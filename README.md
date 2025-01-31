# Just a notes from (mostly) CTF

### Disassemblers
* [IDA](https://www.hex-rays.com/products/ida/) - IDA is a Windows, Linux or Mac OS X hosted multi-processor disassembler and debugger that offers so many features it is hard to describe them all. Just grab an evaluation version if you want a test drive.
* [Ghidra](https://ghidra-sre.org/) - Ghidra is a software reverse engineering (SRE) framework created and maintained by the National Security Agency Research Directorate. Windows, Mac OS, and Linux. Capabilities include disassembly, assembly, decompilation, graphing, and scripting, along with hundreds of other features. Ghidra supports a wide variety of process instruction sets and executable formats and can be run in both user-interactive and automated modes. Users may also develop their own Ghidra plug-in components and/or scripts using Java or Python.
* [radare2](http://radare.org/y/) - Radare2 is an open source tool to disassemble, debug, analyze and manipulate binary files. It actually supports many architectures (x86{16,32,64}, Dalvik, avr, ARM, java, PowerPC, Sparc, MIPS) and several binary formats (pe{32,64}, [fat]mach0{32,64}, ELF{32,64}, dex and Java classes), apart from support for filesystem images and many more features. It runs on the command line, but it has a graphical interface called Cutter that has support for some of its features already.
* [Binary Ninja](https://binary.ninja/) - Binary Ninja is a reverse engineering platform. It focuses on a clean and easy to use interface with a powerful multithreaded analysis built on a custom IL to quickly adapt to a variety of architectures, platforms, and compilers. Runs on macOS, Windows, and Linux.
* [Hopper](http://www.hopperapp.com/) - Hopper is a reverse engineering tool for macOS and Linux, that lets you disassemble, decompile and debug (OS X only) your 32/64bits Intel Mac, Windows and iOS (ARM) executables.
* [x64dbg](http://x64dbg.com/) - An open-source x64/x32 debugger for windows.
* [ImmunityDbg](http://www.immunityinc.com/products/debugger/) - Immunity Debugger is a branch of OllyDbg v1.10, with built-in support for Python scripting and much more.
* [PE Explorer's disassembler](http://www.heaventools.com/PE_Explorer_disassembler.htm) - The PE Explorer Disassembler is designed to be easy to use compared with other disassemblers. To that end, some of the functionality found in other products has been left out in order to keep the process simple and fast. While as powerful as the more expensive, dedicated disassemblers, PE Explorer focuses on ease of use, clarity and navigation.
* [Hiew](http://www.hiew.ru/) - Hiew is a great disassembler designed for hackers, as the name suggests. It supports three modes - Text, Hexadecimal and Decode (Dis-assembly) mode.
* [ODA](http://www.onlinedisassembler.com/) - The Online Disassembler is a free web-based, reverse engineering platform that supports over 60 architectures and object file formats from all the major operating systems, including Windows, Mac OS X, Linux, and mobile platforms.
* [Relyze](https://www.relyze.com/overview.html) - Relyze is a commercial interactive disassembler for x86, x64 and ARM software with loaders for PE or ELF file formats. It supports interactive flat and graph views of the disassembly, generating call and reference graphs, binary diffing two executables, exploring the executable file's structure and a Ruby plugin API. It can also handle things like symbols (PDB's), function local variables, switch statements, exception handlers, static library identification and more.
* [Medusa](https://github.com/wisk/medusa) - Medusa is an open source disassembler with x86, x64, z80 and partial ARM support. It runs on Windows and Linux. It has interactive flat and graph views.
* [W32Dasm](http://www.softpedia.com/get/Programming/Debuggers-Decompilers-Dissasemblers/WDASM.shtml) - W32DASM was an excellent 16/32 bit disassembler for Windows, it seems it is no longer developed. the latest version available is from 2003
* [Capstone](http://www.capstone-engine.org/) - Capstone is a lightweight multi-platform, multi-architecture disassembly framework.
* [BORG Disassembler](http://www.caesum.com/download.php) - BORG is an excellent Win32 Disassembler with GUI.
* [DSM Studio Disassembler](http://www.softpedia.com/get/Programming/Debuggers-Decompilers-Dissasemblers/DSM-Studio.shtml) - DSM Studio is an easy-to-use yet comprehensive application that can aid you in the disassembly and inspection of executables built for the Intel x86 architecture.
* [Decompiler](http://www.softpedia.com/get/Programming/Debuggers-Decompilers-Dissasemblers/Decompiler.shtml) - Decompiler is an easy to use and simply application designed to read program binaries and decompile executable or DLL files. The application is designed to decompile executables for any processor architecture and not be tied to a particular instruction set. Although currently only a x86 front end is implemented, there is nothing preventing you from implementing a 68K, Sparc, or VAX front end if you need one.
* [Lida - linux interactive disassembler](http://sourceforge.net/projects/lida/) - lida is a fast feature packed interactive ELF disassembler / code-/cryptoanalyzer based on bastards libdisasm
* [BugDbg x64 v0.7.5](http://www.pespin.com/) - BugDbg x64 is a user-land debugger designed to debug native 64-bit applications. BugDbg is released as Freeware.
* [distorm3](http://www.ragestorm.net/distorm/) - A lightweight, Easy-to-Use and Fast Disassembler/Decomposer Library for x86/AMD64
* [Udis86](http://udis86.sourceforge.net/) - Udis86 is an easy-to-use, minimalistic disassembler library (libudis86) for the x86 class of instruction set architectures. It has a convenient interface for use in the analysis and instrumentation of binary code.
* [BeaEngine](http://www.beaengine.org/) - This project is a package with a multi-platform x86 and x64 disassembler library (Solaris, MAC OSX, AIX, Irix, OS/2, Linux, Windows)
* [C4 Decompiler](http://www.c4decompiler.com/) - General Machine Code to C Decompiler, Free Windows I64 target edition, Interactive Windows GUI
* [REC Studio 4 - Reverse Engineering Compiler](http://www.backerstreet.com/rec/rec.htm) - REC Studio is an interactive decompiler. It reads a Windows, Linux, Mac OS X or raw executable file, and attempts to produce a C-like representation of the code and data used to build the executable file. It has been designed to read files produced for many different targets, and it has been compiled on several host systems.
* [Retargetable Decompiler](https://retdec.com/) - A retargetable decompiler that can be utilized for source code recovery, static malware analysis, etc. The decompiler is supposed to be not bounded to any particular target architecture, operating system, or executable file format.
* [miasm](http://fcml-lib.com/index.html) - Miasm is a a free and open source (GPLv2) reverse engineering framework written in python. Miasm aims at analyzing/modifying/generating binary programs.
* [Free Code Manipulation Library](http://fcml-lib.com/index.html) - This is a general purpose machine code manipulation library for IA-32 and Intel 64 architectures. The library supports UNIX-like systems as well as Windows and is highly portable.
* [Intel® X86 Encoder Decoder Software Library](https://software.intel.com/en-us/articles/xed-x86-encoder-decoder-software-library) - Intel® XED is a software library (and associated headers) for encoding and decoding X86 (IA32 and Intel64) instructions.
* [angr](http://angr.io/) - angr is a framework for analyzing binaries. It focuses on both static and dynamic symbolic ("concolic") analysis, making it applicable to a variety of tasks.
* [JEB Decompiler](https://www.pnfsoftware.com/jeb2/) - JEB is a reverse-engineering platform to perform disassembly, decompilation, debugging, and analysis of code and document files, manually or as part of an analysis pipeline.
* [Cutter](https://github.com/radareorg/cutter) - A Qt and C++ GUI for radare2 reverse engineering framework (originally Iaito). Cutter is not aimed at existing radare2 users. It instead focuses on those whose are not yet radare2 users because of the learning curve, because they don't like CLI applications or because of the difficulty/instability of radare2.
* [REDasm](https://github.com/REDasmOrg/REDasm) - REDasm is an interactive, multiarchitecture disassembler written in C++ using Qt5 as UI Framework. Its core is light and simple, it can be extended in order to support new instruction sets and file formats.


### Offline
* [CeWL - Custom Word List generator](https://digi.ninja/projects/cewl.php) | [github](https://github.com/digininja/CeWL)
* [Nmap: the Network Mapper - Free Security Scanner](https://nmap.org/)
* [p0f - passive TCP/IP stack fingerprinting tool](http://lcamtuf.coredump.cx/p0f3/)
* [cURL](https://curl.haxx.se/)


### Online
* [Steganography Tools](http://futureboy.us/stegano/)
* [Online Disassembler](https://onlinedisassembler.com)
* [Cyber Chef](https://gchq.github.io/CyberChef/)


### Reverse engineering
* [OnlineGDB](https://www.onlinegdb.com) - online compiler and debugger for c/c++
* [Jump instructions](https://faydoc.tripod.com/cpu/index_j.htm)


### OSINT
* [Shademap](https://shademap.app) - Simulator of a shade
* [how to find a location using only the shadow](https://www.youtube.com/watch?v=pQIjDPFgdJA)


### Cracking
* [Weakpass](https://weakpass.com) - Weakpass.com is a collection of password lists for various purposes from penetration testing to improving password security.


### Various
* [evilginx2](https://github.com/kgretzky/evilginx2) 
* [Modlishka. Reverse Proxy. Phishing NG.](https://github.com/drk1wi/Modlishka) 
* [hasherezade](https://github.com/hasherezade) 
* [Windows Exploit Suggester](https://github.com/bitsadmin/wesng)
* [Ghidra - software reverse engineering framework](https://github.com/NationalSecurityAgency/ghidra)
* [Is website vulnerable](https://github.com/lirantal/is-website-vulnerable) - finds publicly known security vulnerabilities in a website's frontend JavaScript libraries
* [Frida](https://frida.re/docs/quickstart/) - Dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers.


### Blogs / websites
* [hasherezade](https://hshrzd.wordpress.com/) 
* [Awesome Bug Bounty](https://github.com/djadmin/awesome-bug-bounty)
* [PL - Adam Kostrzewa - Blog about Security and Embedded Design](https://adamkostrzewa.github.io/)
* [DARKNET DIARIES](https://darknetdiaries.com/) - True stories from the dark side of the Internet. This is a podcast about hackers, breaches, APTs, hacktivism, cybercrime, and all the things that dwell on the hidden parts of the network. This is Darknet Diaries.

### Tutorials / Articles / Other
* [PL/Youtube - Od 0 do pentestera](https://www.youtube.com/channel/UCP16m86ciUUlU8UZvlpw0TQ)
* [Security and Docker: tips and tricks](https://made2591.github.io/posts/docker-security)
* [Kali Linux Penetration Testing Tools](https://tools.kali.org/)
* [Cracking PDF with John the Ripper](https://medium.com/@baodad/cracking-my-first-password-8df292fc71c5)
* [Programming languages infosec professionals should learn](https://blog.erratasec.com/2019/04/programming-languages-infosec.html#.XL3WGy-B2L4)
* [How I hacked Google’s bug tracking system itself for $15,600 in bounties](https://medium.com/free-code-camp/messing-with-the-google-buganizer-system-for-15-600-in-bounties-58f86cc9f9a5)

### CTF
* [CTF Resources](http://ctfs.github.io/resources/)
* [Input validation](https://medium.com/@en3sec/ryans-ctf-input-validation-90c03c58235f)
* [Linux Reverse Engineering CTFs for Beginners](https://osandamalith.com/2019/02/11/linux-reverse-engineering-ctfs-for-beginners/)
* [A good general CTF guide](https://www.reddit.com/r/hacking/comments/awc9u7/a_good_general_ctf_guide/)
* [$50 million CTF Writeup](https://github.com/manoelt/50M_CTF_Writeup/blob/master/README.md)

### Android
* [How does Dalvik handle 'this' registers?](https://calebfenton.github.io/2016/02/21/how-does-dalvik-handle-this-registers/) 
* [Registers in Dalvik](https://github.com/JesusFreke/smali/wiki/Registers) 
* [Android Reverse Engineering: Debugging Smali in Smalidea](https://crosp.net/blog/software-development/mobile/android/android-reverse-engineering-debugging-smali-using-smalidea/) 
* [Dalvik bytecode](https://source.android.com/devices/tech/dalvik/dalvik-bytecode) 
* [How to capture Bluetooth packets on Android 4.4](https://www.nowsecure.com/blog/2014/02/07/bluetooth-packet-capture-on-android-4-4/) 
* [XPrivacyLua](https://github.com/M66B/XPrivacyLua) - Really simple to use privacy manager for Android 6.0 Marshmallow and later

### Privacy
* [Privacy tools](https://www.privacytools.io/classic/) - List of privacy tools

### Other
* [zip bomb](https://www.bamsoftware.com/hacks/zipbomb/)