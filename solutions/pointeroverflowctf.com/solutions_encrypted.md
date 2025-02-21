Solutions are encrypted with base64
use this script to decode it
```
python ../flags.py solutions_encrypted.md --flag-format poctf{xxx} --mode=decrypt
```

### Cracking
<pre>
Crack 100 - No Thing Lasts Forever              not solved
-> john the ripper
-> zip2john.exe Crack100-1.zip > hash.txt
-> john hash.txt

Crypto 200 - Knuckle Buster                     poctf{dXdzcF9mMXIzXzRuZF9icjFtNTcwbjM=}
Crypto 200 - Everyone's Friend                  poctf{dXdzcF83aDNfaDE3Y2hoMWszcjVfNnUxZDM=}
</pre>

### Forensic
<pre>
DF 100 - A Record of Events                     not solved
DF 100 - A Flat Circle                          not solved
hint: Simple multimedia forensics challenge. Just process the image and you will come across the flag.
DF 100 - I've Been There Too                    poctf{dXdzcF9kMF80bmRyMDFkNV9kcjM0bQ==}
-> Any sqlite browser
</pre>

### MISC
<pre>
Misc 100 - I Never Knew Glory                   poctf{dXdzcF8wbmMzX20wcjNfdW43MF83aDNfYnIzNGNo}
Misc 100 - Could It Be the Winter               poctf{dXdzcF95MHVfc2g0MTFfbjA3X3A0NTU=}
Misc 200 - Anything Worth Doing Wrong           poctf{dXdzcF9wNHI3MW42XzE1XzV1Y2hfNXczMzdfNTBycjB3}
Misc 200 - Embrace the Suck                     poctf{dXdzcF83aDMgbjMzZDUgMGYgN2gzIHI0bmM=}
-> substitution cipher
Misc 200 - My Name is Human                     poctf{dXdzcF9DUllfSDRWMEM=}
Misc 300 - The Hollow Howl of Foreign Winds     poctf{dXdzcF8xXzRtX2IzYzBtM19kMzQ3aA==}
Misc 300 - Beneath the Pea Beneath the Pillow   poctf{dXdzcF9oM2xsX2g0N2hfbjBfZnVyeQ==}
-> height == letter no. more or less
</pre>

### OSINT
<pre>
OSINT 100 - Who Can It Be Now                   poctf{dXdzcF9sM19wNDFuX3F1MDcxZDEzbg==}
OSINT 300 - Down Like This                      poctf{dXdzcF83aDNfNG41dzNyXzcwXzN2M3J5N2gxbjY=}
OSINT-200 Grifting Lonesome Widowers            not solved
</pre>
hint: The challenge text uses a lot of odd lingo. If you look into it, it's clear I'm a poker player. Or at least I know the slang. I wonder what the odd language our blackmailer uses means?


### Stegano
<pre>
Stego 100 - Things Seen and Unseen              poctf{dXdzcF93aDQ3XzE1X2QzNGRfbTR5X24zdjNyX2QxMw==}
Stego 100 - Things Said and Unsaid              poctf{dXdzcF93M180cjNfc3VjaF81N3VmZg==}
-> https://aperisolve.com
-> foremost
-> probably_improbable
</pre>

### Web
<pre>
Web 100 - The Way Out is Through            poctf{dXdzcF83aDNfN3J1N2hfMTVfMHU3XzdoM3Iz}
Web 200 - Gifting a White Elephant          poctf{dXdzcF80X2ZyMTNuZF83MF80bGw=}
-> curl -A "FBI-SiteAccess-Authorized-Agent" http://34.135.223.176:6007/agent-access
Web 200 - On My Own Terms                   poctf{dXdzcF93M180cjNfd2g0N193M183aDFuaw==}
-> cookie user->admin
</pre>

### Reverse
<pre>
Reverse 100 - End of the Line               poctf{dXdzcF9kMF8wcl9kMF9uMDc=}
-> offset used to obfuscate the answer. can be decoded from assembly
Reverse 200 - We Do It Live                 poctf{dXdzcF83aDNfbjE2aDdfMTVfZDRyaw==}
-> offset used to obfuscate the answer.
Reverse 300 - Separating the Firmament      poctf{dXdzcF83aDNfdzBybGRfMTVfNF81NzQ2Mw==}
-> IDA => jz<->jnz
Reverse 300 - Think Different, Be Similar   poctf{dXdzcF80YjRuZDBuXzRsbF9oMHAz}
-> Wireshark ;-)
</pre>

### Notes

@CTF_Participant We must issue a notice for all participants. One of the flags for the available challenges includes an error. One of them includes several lowercase 'e' charactrers when the character set specified in the rules substitutes that character for a '3.' We apologize for the error, and you may submit the flag as you find it to earn points.

That wouldn't be fair to everyone. I would need to share it with everyone. So here - this is probably it. poctf{dXdzcF8xNV83aDE1XzRfbWVtZT8=} Yeah. 'e' instead of '3' that must be it. 
