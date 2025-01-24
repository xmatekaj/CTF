### Cracking
Crack 100 - No Thing Lasts Forever              not solved
-> john the ripper
-> zip2john.exe Crack100-1.zip > hash.txt
-> john hash.txt

Crypto 200 - Knuckle Buster                     poctf{uwsp_f1r3_4nd_br1m570n3}
Crypto 200 - Everyone's Friend                  poctf{uwsp_7h3_h17chh1k3r5_6u1d3}
===============================================
### Forensic
DF 100 - A Record of Events                     not solved
DF 100 - A Flat Circle                          not solved
hint: Simple multimedia forensics challenge. Just process the image and you will come across the flag.
DF 100 - I've Been There Too                    poctf{uwsp_d0_4ndr01d5_dr34m}
-> Any sqlite browser
===============================================
### MISC
Misc 100 - I Never Knew Glory                   poctf{uwsp_0nc3_m0r3_un70_7h3_br34ch}
Misc 100 - Could It Be the Winter               poctf{uwsp_y0u_sh411_n07_p455}
Misc 200 - Anything Worth Doing Wrong           poctf{uwsp_p4r71n6_15_5uch_5w337_50rr0w}
Misc 200 - Embrace the Suck                     poctf{uwsp_7h3 n33d5 0f 7h3 r4nc}
-> substitution cipher
Misc 200 - My Name is Human                     poctf{uwsp_CRY_H4V0C}
Misc 300 - The Hollow Howl of Foreign Winds     poctf{uwsp_1_4m_b3c0m3_d347h}
Misc 300 - Beneath the Pea Beneath the Pillow   poctf{uwsp_h3ll_h47h_n0_fury}
-> height == letter no. more or less
===============================================
### OSINT
OSINT 100 - Who Can It Be Now                   poctf{uwsp_l3_p41n_qu071d13n}
OSINT 300 - Down Like This                      poctf{uwsp_7h3_4n5w3r_70_3v3ry7h1n6}
OSINT-200 Grifting Lonesome Widowers            not solved
hint: The challenge text uses a lot of odd lingo. If you look into it, it's clear I'm a poker player. Or at least I know the slang. I wonder what the odd language our blackmailer uses means?
===============================================
Stego 100 - Things Seen and Unseen              poctf{uwsp_wh47_15_d34d_m4y_n3v3r_d13}
Stego 100 - Things Said and Unsaid              poctf{uwsp_w3_4r3_such_57uff}
-> https://aperisolve.com
-> foremost
-> probably_improbable
===============================================
### Web
Web 100 - The Way Out is Through            poctf{uwsp_7h3_7ru7h_15_0u7_7h3r3}
Web 200 - Gifting a White Elephant          poctf{uwsp_4_fr13nd_70_4ll}
-> curl -A "FBI-SiteAccess-Authorized-Agent" http://34.135.223.176:6007/agent-access
Web 200 - On My Own Terms                   poctf{uwsp_w3_4r3_wh47_w3_7h1nk}
-> cookie user->admin
===============================================
### Reverse
Reverse 100 - End of the Line               poctf{uwsp_d0_0r_d0_n07}
-> offset used to obfuscate the answer. can be decoded from assembly
Reverse 200 - We Do It Live                 poctf{uwsp_7h3_n16h7_15_d4rk}
-> offset used to obfuscate the answer.
Reverse 300 - Separating the Firmament      poctf{uwsp_7h3_w0rld_15_4_57463}
-> IDA => jz<->jnz
Reverse 300 - Think Different, Be Similar   poctf{uwsp_4b4nd0n_4ll_h0p3}
-> Wireshark ;-)
===============================================
## Notes
@CTF_Participant We must issue a notice for all participants. One of the flags for the available challenges includes an error. One of them includes several lowercase 'e' charactrers when the character set specified in the rules substitutes that character for a '3.' We apologize for the error, and you may submit the flag as you find it to earn points.

That wouldn't be fair to everyone. I would need to share it with everyone. So here - this is probably it. poctf{uwsp_15_7h15_4_meme?} Yeah. 'e' instead of '3' that must be it. 