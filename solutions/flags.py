#!/usr/bin/env python3
import base64
import re
import sys
import argparse
import os

def extract_flag_content(flag, flag_format):
    """Extract the content inside curly braces from a flag."""
    # Create pattern that captures the content inside curly braces
    prefix = flag_format.split('{')[0]
    pattern = f"{prefix}" + r"\{([^}]+)\}"
    match = re.match(pattern, flag)
    if match:
        return match.group(1)
    return None

def encrypt_flag_content(content):
    """Encrypt flag content using base64."""
    return base64.b64encode(content.encode()).decode()

def decrypt_flag_content(encrypted_content):
    """Decrypt base64 encoded flag content."""
    try:
        return base64.b64decode(encrypted_content.encode()).decode()
    except:
        print(f"Warning: Could not decrypt '{encrypted_content}' - keeping original")
        return encrypted_content

def process_flag(flag, flag_format, mode='encrypt'):
    """Process a single flag while preserving its format."""
    content = extract_flag_content(flag, flag_format)
    if content is None:
        return flag
        
    prefix = flag_format.split('{')[0]
    if mode == 'encrypt':
        processed_content = encrypt_flag_content(content)
    else:
        processed_content = decrypt_flag_content(content)
        
    return f"{prefix}{{{processed_content}}}"

def extract_and_process_flags(content, flag_format, mode='encrypt'):
    """Extract flags from the content and replace them with processed versions."""
    # Escape special regex characters in the flag format
    escaped_format = re.escape(flag_format)
    # Replace {xxx} with a regex pattern that matches any characters within curly braces
    pattern = escaped_format.replace('\\{xxx\\}', '\\{[^}]+\\}')
    
    def replace_func(match):
        flag = match.group(0)
        return process_flag(flag, flag_format, mode)
    
    # Replace all flags in the content
    new_content = re.sub(pattern, replace_func, content)
    return new_content

def process_file(filename, flag_format, mode='encrypt'):
    """Process the file, replacing flags and saving to a new file."""
    try:
        # Read the input file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Process the content
        processed_content = extract_and_process_flags(content, flag_format, mode)
        
        # Generate output filename
        base_name, ext = os.path.splitext(filename)
        suffix = '_encrypted' if mode == 'encrypt' else '_decrypted'
        output_filename = f"{base_name}{suffix}{ext}"
        
        # Save the processed content
        with open(output_filename, 'w') as file:
            file.write(processed_content)
            
        print(f"Successfully processed file. Output saved to: {output_filename}")
        
        # Count processed flags
        original_flags = re.findall(flag_format.replace('xxx', '[^}]+'), content)
        print(f"Processed {len(original_flags)} flags")
                
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error processing file: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Encrypt/Decrypt CTF flags in a file using base64')
    parser.add_argument('filename', help='The file to process')
    parser.add_argument('--flag-format', default='poctf{xxx}', 
                        help='The format of flags to look for (default: poctf{xxx})')
    parser.add_argument('--mode', choices=['encrypt', 'decrypt'], default='encrypt',
                        help='Whether to encrypt or decrypt flags (default: encrypt)')
    
    args = parser.parse_args()
    
    process_file(args.filename, args.flag_format, args.mode)

if __name__ == "__main__":
    main()