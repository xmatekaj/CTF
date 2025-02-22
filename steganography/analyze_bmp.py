import numpy as np
from PIL import Image
import os
from datetime import datetime

class BMPAnalyzer:
    def __init__(self, file_path):
        """Initialize the BMP analyzer with a file path."""
        self.file_path = file_path
        self.analysis_results = {}
        self.file_size = os.path.getsize(file_path)
        
        # Create output directory
        self.output_dir = f"bmp_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.makedirs(self.output_dir, exist_ok=True)

    def save_results(self, section, data):
        """Save analysis results to the class dictionary."""
        self.analysis_results[section] = data

    def analyze_file_structure(self):
        """Analyze the basic file structure and headers."""
        with open(self.file_path, 'rb') as f:
            # Read headers
            file_header = f.read(14)
            dib_header = f.read(124)

            # Extract file header information
            file_info = {
                'signature': file_header[0:2].decode('ascii'),
                'file_size': int.from_bytes(file_header[2:6], 'little'),
                'reserved1': int.from_bytes(file_header[6:8], 'little'),
                'reserved2': int.from_bytes(file_header[8:10], 'little'),
                'pixel_offset': int.from_bytes(file_header[10:14], 'little')
            }

            # Extract DIB header information
            dib_info = {
                'header_size': int.from_bytes(dib_header[0:4], 'little'),
                'width': int.from_bytes(dib_header[4:8], 'little'),
                'height': int.from_bytes(dib_header[8:12], 'little'),
                'planes': int.from_bytes(dib_header[12:14], 'little'),
                'bpp': int.from_bytes(dib_header[14:16], 'little'),
                'compression': int.from_bytes(dib_header[16:20], 'little'),
                'image_size': int.from_bytes(dib_header[20:24], 'little'),
                'x_ppm': int.from_bytes(dib_header[24:28], 'little'),
                'y_ppm': int.from_bytes(dib_header[28:32], 'little'),
                'colors_used': int.from_bytes(dib_header[32:36], 'little'),
                'important_colors': int.from_bytes(dib_header[36:40], 'little'),
                'red_mask': dib_header[40:44].hex(),
                'green_mask': dib_header[44:48].hex(),
                'blue_mask': dib_header[48:52].hex(),
                'alpha_mask': dib_header[52:56].hex()
            }

            # Calculate expected sizes
            expected_pixel_data_size = dib_info['width'] * dib_info['height'] * (dib_info['bpp'] // 8)
            expected_total_size = file_info['pixel_offset'] + expected_pixel_data_size
            size_discrepancy = self.file_size - expected_total_size

            # Add size analysis
            size_analysis = {
                'actual_size': self.file_size,
                'expected_size': expected_total_size,
                'discrepancy': size_discrepancy,
                'has_extra_data': size_discrepancy > 0
            }

            self.save_results('file_structure', {
                'file_header': file_info,
                'dib_header': dib_info,
                'size_analysis': size_analysis
            })

    def analyze_pixel_data(self):
        """Analyze the actual pixel data of the image."""
        img = Image.open(self.file_path)
        img_array = np.array(img)

        # Basic image statistics
        channels = []
        channel_names = ['Red', 'Green', 'Blue', 'Alpha'] if img_array.shape[-1] == 4 else ['Red', 'Green', 'Blue']
        
        for i, channel_name in enumerate(channel_names):
            channel = img_array[:,:,i]
            channel_stats = {
                'name': channel_name,
                'min': int(channel.min()),
                'max': int(channel.max()),
                'mean': float(channel.mean()),
                'median': float(np.median(channel)),
                'std': float(channel.std()),
                'unique_values': len(np.unique(channel))
            }
            channels.append(channel_stats)

            # Save individual channel images
            channel_img = Image.fromarray(channel)
            channel_img.save(os.path.join(self.output_dir, f'{channel_name.lower()}_channel.png'))

        self.save_results('pixel_analysis', {
            'dimensions': img_array.shape,
            'channels': channels
        })

    def analyze_hidden_data(self):
        """Look for potential hidden data in the file using multiple methods."""
        with open(self.file_path, 'rb') as f:
            # Get file structure info
            file_struct = self.analysis_results['file_structure']
            expected_end = file_struct['file_header']['pixel_offset'] + \
                          file_struct['dib_header']['width'] * \
                          file_struct['dib_header']['height'] * \
                          (file_struct['dib_header']['bpp'] // 8)

            hidden_data_analysis = {
                'has_extra_data': False,
                'extra_data_size': 0,
                'potential_hidden_image': False,
                'strings_found': [],
                'binwalk_results': []
            }

            if self.file_size > expected_end:
                # There's extra data
                hidden_data_analysis['has_extra_data'] = True
                hidden_data_analysis['extra_data_size'] = self.file_size - expected_end

                # Read the extra data
                f.seek(expected_end)
                extra_data = f.read()

                # Try to detect and process hidden image
                self._process_hidden_image(extra_data, hidden_data_analysis)
                
                # Run strings analysis
                self._analyze_strings(extra_data, hidden_data_analysis)
                
                # Run binwalk if available
                self._run_binwalk(hidden_data_analysis)

            self.save_results('hidden_data', hidden_data_analysis)

    def _process_hidden_image(self, extra_data, analysis_results):
        """Process potential hidden image data with various transformations."""
        if len(extra_data) >= 512 * 512 * 4:  # Check for minimum size for 512x512 RGBA
            try:
                # Reshape into 512x512 image
                image_array = np.frombuffer(extra_data[:512*512*4], dtype=np.uint8).reshape((512, 512, 4))
                
                # Create a larger canvas with padding
                padded_size = 768
                padded_array = np.zeros((padded_size, padded_size, 4), dtype=np.uint8)
                
                # Calculate padding
                start_x = (padded_size - 512) // 2
                start_y = (padded_size - 512) // 2
                
                # Place original image in center of padded array
                padded_array[start_y:start_y+512, start_x:start_x+512] = image_array
                
                # Save original hidden image
                Image.fromarray(image_array, 'RGBA').save(
                    os.path.join(self.output_dir, 'hidden_original.png')
                )
                
                # All possible flip combinations
                flip_transformations = [
                    ('h', np.flip(padded_array, axis=1)),  # Horizontal
                    ('v', np.flip(padded_array, axis=0)),  # Vertical
                    ('vh', np.flip(np.flip(padded_array, axis=0), axis=1))  # Both
                ]
                
                for flip_type, flipped_array in flip_transformations:
                    # Save normal flipped version
                    Image.fromarray(flipped_array, 'RGBA').save(
                        os.path.join(self.output_dir, f'hidden_flipped_{flip_type}_padded.png')
                    )
                    
                    # Create and save inverted version
                    inverted = 255 - flipped_array[:, :, :3]
                    inverted_rgba = np.dstack((inverted, flipped_array[:, :, 3]))
                    Image.fromarray(inverted_rgba, 'RGBA').save(
                        os.path.join(self.output_dir, f'hidden_inverted_flipped_{flip_type}_padded.png')
                    )
                
                # Enhanced contrast versions for each channel
                for channel_idx, channel_name in enumerate(['red', 'green', 'blue']):
                    channel = padded_array[:, :, channel_idx].astype(float)
                    min_val = np.percentile(channel, 5)
                    max_val = np.percentile(channel, 95)
                    enhanced = np.clip((channel - min_val) * (255.0/(max_val - min_val)), 0, 255).astype(np.uint8)
                    
                    # Save enhanced versions with all flip combinations
                    for flip_type, _ in flip_transformations:
                        flipped_enhanced = np.flip(enhanced, axis=0 if 'v' in flip_type else 1)
                        if 'vh' in flip_type:
                            flipped_enhanced = np.flip(flipped_enhanced, axis=1)
                        Image.fromarray(flipped_enhanced).save(
                            os.path.join(self.output_dir, f'hidden_enhanced_{channel_name}_flipped_{flip_type}.png')
                        )
                
                analysis_results['potential_hidden_image'] = True
                analysis_results['hidden_image_size'] = '512x512'
                analysis_results['transformations_applied'] = [
                    'original',
                    'horizontal_flip',
                    'vertical_flip',
                    'vertical_horizontal_flip',
                    'inverted',
                    'enhanced_contrast'
                ]
            
            except Exception as e:
                print(f"Error processing hidden image: {str(e)}")

    def _analyze_strings(self, data, analysis_results):
        """Analyze data for ASCII and Unicode strings."""
        def is_printable(s):
            return all(32 <= ord(c) <= 126 or c in '\n\r\t' for c in s)
        
        # Look for ASCII strings
        ascii_strings = []
        current_string = ''
        min_length = 4  # Minimum string length to consider
        
        # ASCII search
        for byte in data:
            try:
                char = chr(byte)
                if is_printable(char):
                    current_string += char
                elif len(current_string) >= min_length:
                    ascii_strings.append(current_string)
                    current_string = ''
                else:
                    current_string = ''
            except:
                if len(current_string) >= min_length:
                    ascii_strings.append(current_string)
                current_string = ''
        
        # Unicode search (UTF-16)
        unicode_strings = []
        try:
            unicode_data = data.decode('utf-16')
            unicode_strings = [s for s in unicode_data.split('\x00') if len(s) >= min_length and is_printable(s)]
        except:
            pass
        
        # Save results
        analysis_results['strings_found'] = {
            'ascii': ascii_strings,
            'unicode': unicode_strings
        }
        
        # Save strings to file
        strings_file = os.path.join(self.output_dir, 'extracted_strings.txt')
        with open(strings_file, 'w', encoding='utf-8') as f:
            f.write("=== ASCII Strings ===\n")
            for s in ascii_strings:
                f.write(f"{s}\n")
            f.write("\n=== Unicode Strings ===\n")
            for s in unicode_strings:
                f.write(f"{s}\n")

    def _run_binwalk(self, analysis_results):
        """Run binwalk analysis if available."""
        try:
            import binwalk
            
            print("Running binwalk analysis...")
            results = []
            
            for module in binwalk.scan(self.file_path, signature=True, quiet=True):
                for result in module.results:
                    results.append({
                        'offset': result.offset,
                        'description': result.description,
                        'size': getattr(result, 'size', 'unknown')
                    })
            
            analysis_results['binwalk_results'] = results
            
            # Save detailed binwalk results
            binwalk_file = os.path.join(self.output_dir, 'binwalk_results.txt')
            with open(binwalk_file, 'w') as f:
                f.write("=== Binwalk Analysis Results ===\n")
                for result in results:
                    f.write(f"Offset: {result['offset']}\n")
                    f.write(f"Description: {result['description']}\n")
                    f.write(f"Size: {result['size']}\n")
                    f.write("-" * 50 + "\n")
                    
        except ImportError:
            analysis_results['binwalk_results'] = "Binwalk not available. Install with 'pip install binwalk'"

    def analyze_lsb(self):
        """Analyze Least Significant Bits for potential steganography."""
        img = Image.open(self.file_path)
        img_array = np.array(img)

        lsb_analysis = {}
        for i, channel in enumerate(['red', 'green', 'blue']):
            # Extract LSB
            lsb = img_array[:,:,i] & 1
            
            # Save LSB image
            lsb_img = Image.fromarray((lsb * 255).astype(np.uint8))
            lsb_img.save(os.path.join(self.output_dir, f'{channel}_lsb.png'))
            
            # Analyze LSB patterns
            lsb_analysis[channel] = {
                'unique_patterns': len(np.unique(lsb)),
                'ones_percentage': (lsb == 1).mean() * 100,
                'entropy': float(np.abs(np.fft.fft2(lsb)).std())
            }

        self.save_results('lsb_analysis', lsb_analysis)

    def generate_report(self):
        """Generate a comprehensive report of all analyses."""
        report = []
        
        # File Structure Section
        fs = self.analysis_results['file_structure']
        report.append("=== BMP File Analysis Report ===\n")
        
        report.append("1. Basic File Information:")
        report.append(f"   - File: {os.path.basename(self.file_path)}")
        report.append(f"   - Size: {self.file_size:,} bytes")
        report.append(f"   - Signature: {fs['file_header']['signature']}")
        
        report.append("\n2. Image Properties:")
        dib = fs['dib_header']
        report.append(f"   - Dimensions: {dib['width']}x{dib['height']} pixels")
        report.append(f"   - Bit Depth: {dib['bpp']} bits per pixel")
        report.append(f"   - Compression: {dib['compression']}")
        
        # Pixel Analysis Section
        pa = self.analysis_results['pixel_analysis']
        report.append("\n3. Channel Analysis:")
        for channel in pa['channels']:
            report.append(f"\n   {channel['name']} Channel:")
            report.append(f"   - Range: {channel['min']} to {channel['max']}")
            report.append(f"   - Mean: {channel['mean']:.2f}")
            report.append(f"   - Unique Values: {channel['unique_values']}")
        
        # Hidden Data Analysis
        hd = self.analysis_results['hidden_data']
        report.append("\n4. Hidden Data Analysis:")
        if hd['has_extra_data']:
            report.append(f"   - Extra Data Found: {hd['extra_data_size']:,} bytes")
            
            if hd['potential_hidden_image']:
                report.append(f"   - Hidden image detected ({hd['hidden_image_size']})")
                report.append("   - Applied transformations:")
                for transform in hd['transformations_applied']:
                    report.append(f"     * {transform}")
            
            if 'strings_found' in hd and isinstance(hd['strings_found'], dict):
                ascii_count = len(hd['strings_found']['ascii'])
                unicode_count = len(hd['strings_found']['unicode'])
                report.append(f"   - Strings found: {ascii_count} ASCII, {unicode_count} Unicode")
                report.append("     (See 'extracted_strings.txt' for details)")
            
            if 'binwalk_results' in hd:
                if isinstance(hd['binwalk_results'], list):
                    report.append(f"   - Binwalk found {len(hd['binwalk_results'])} signatures:")
                    for result in hd['binwalk_results'][:5]:  # Show first 5 results
                        report.append(f"     * At offset {result['offset']}: {result['description']}")
                    if len(hd['binwalk_results']) > 5:
                        report.append("     (See 'binwalk_results.txt' for full results)")
                else:
                    report.append(f"   - Binwalk: {hd['binwalk_results']}")
        else:
            report.append("   - No extra data found")
        
        # LSB Analysis
        lsb = self.analysis_results['lsb_analysis']
        report.append("\n5. LSB Steganography Analysis:")
        for channel, data in lsb.items():
            report.append(f"   {channel.capitalize()} channel:")
            report.append(f"   - Unique patterns: {data['unique_patterns']}")
            report.append(f"   - Ones percentage: {data['ones_percentage']:.2f}%")
            report.append(f"   - Pattern entropy: {data['entropy']:.2f}")

        # Dimension Analysis
        dim = self.analysis_results.get('dimensions', {})
        if dim:
            report.append("\n6. Dimension Analysis:")
            report.append(f"   Original dimensions: {dim['original_width']}x{dim['original_height']}")
            report.append(f"   File info:")
            report.append(f"   - Total file size: {dim['debug_info']['total_file_bytes']:,} bytes")
            report.append(f"   - Bytes per pixel: {dim['debug_info']['bytes_per_pixel']}")
            report.append(f"   - Header size: {dim['debug_info']['header_size']} bytes")
            report.append("\n   Alternative dimensions tested:")
            for dim_test in sorted(dim['tried_dimensions'], key=lambda x: x['pixels']):
                report.append(f"   - {dim_test['width']}x{dim_test['height']} " +
                            f"({dim_test['pixels']:,} pixels, " +
                            f"requires {dim_test['required_bytes']:,} bytes)")
                report.append(f"     Created as: {dim_test['filename']}")

        report.append("\n7. Generated Files:")
        report.append(f"   Output directory: {self.output_dir}/")
        report.append("   - Channel separations")
        report.append("   - LSB analysis images")
        if hd['potential_hidden_image']:
            report.append("   - Potential hidden images with various transformations:")
            report.append("     * Original and padded versions")
            report.append("     * Horizontal, vertical, and both flips")
            report.append("     * Inverted colors")
            report.append("     * Enhanced contrast per channel")
        report.append("   - Alternative dimension versions")
        report.append("   - String analysis results")
        report.append("   - Binwalk analysis results (if available)")

        # Save report
        report_path = os.path.join(self.output_dir, 'analysis_report.txt')
        with open(report_path, 'w') as f:
            f.write('\n'.join(report))
        
        return '\n'.join(report)

    def analyze_dimensions(self):
        """Try different image dimensions to reveal hidden content."""
        with open(self.file_path, 'rb') as f:
            data = f.read()
        
        # Get original dimensions
        orig_width = int.from_bytes(data[18:22], 'little')
        orig_height = int.from_bytes(data[22:26], 'little')
        
        dimension_analysis = {
            'original_width': orig_width,
            'original_height': orig_height,
            'tried_dimensions': []
        }
        
        # Generate combinations based on original dimensions
        combinations = [
            (orig_width, orig_width),                    # Square using width
            (orig_height, orig_height),                  # Square using height
            (orig_width * 2, orig_height),              # Double width
            (orig_width, orig_height * 2),              # Double height
            (int(orig_width * 1.5), orig_height),       # 1.5x width
            (orig_width, int(orig_height * 1.5)),       # 1.5x height
            (orig_width * 2, int(orig_height * 1.5)),   # 2x width, 1.5x height
            (int(orig_width * 1.5), orig_height * 2),   # 1.5x width, 2x height
        ]
        
        # Calculate total bytes in file
        total_bytes = len(data)
        bpp = int.from_bytes(data[28:30], 'little')  # bits per pixel
        bytes_per_pixel = bpp // 8
        
        # Filter combinations that would exceed file size
        valid_combinations = []
        for width, height in combinations:
            required_bytes = width * height * bytes_per_pixel + 54  # 54 is typical BMP header size
            if required_bytes <= total_bytes:
                valid_combinations.append((width, height))
            
        # Log original values for debugging
        dimension_analysis['debug_info'] = {
            'total_file_bytes': total_bytes,
            'bytes_per_pixel': bytes_per_pixel,
            'header_size': int.from_bytes(data[14:18], 'little')
        }
        
        for width, height in valid_combinations:
            try:
                modified = bytearray(data)
                
                # Set new width
                width_bytes = width.to_bytes(4, 'little')
                modified[18:22] = width_bytes
                
                # Set new height
                height_bytes = height.to_bytes(4, 'little')
                modified[22:26] = height_bytes
                
                # Save modified file
                output_file = os.path.join(self.output_dir, f'dim_{width}x{height}.bmp')
                with open(output_file, 'wb') as f:
                    f.write(modified)
                
                dimension_analysis['tried_dimensions'].append({
                    'width': width,
                    'height': height,
                    'filename': os.path.basename(output_file),
                    'pixels': width * height,
                    'required_bytes': width * height * bytes_per_pixel + 54
                })
                
            except Exception as e:
                print(f"Error creating {width}x{height} version: {str(e)}")
        
        self.save_results('dimensions', dimension_analysis)

    def analyze(self):
        """Run all analyses and generate report."""
        self.analyze_file_structure()
        self.analyze_pixel_data()
        self.analyze_hidden_data()
        self.analyze_lsb()
        self.analyze_dimensions()
        return self.generate_report()

def analyze_bmp(file_path):
    """Convenience function to analyze a BMP file."""
    analyzer = BMPAnalyzer(file_path)
    return analyzer.analyze()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python bmp_analyzer.py <bmp_file>")
        sys.exit(1)
    
    report = analyze_bmp(sys.argv[1])
    print(report)