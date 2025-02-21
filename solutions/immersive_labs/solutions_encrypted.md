### May The Fourth
#### Mal Wars
- flag{ZXZpbGVtcGlyMy5leGU=}
- flag{MzNkYTNhZGZmNDQ4ZmI1OTYzYzUyYmI5Mzk3NzdmN2E=}

#### It's a Trap!
=> https://justhack.in/shell-escapes-cheatsheet
- flag{Y2Q1ZTE0OGVkYjE2OTYwODQ3NzU0MGM4NDc0NWQ4NWE=}

#### Order 66
=> jne (0x14ba)
vi -b order
:!xxd
i
esc
:wq
xxd -r order order2
chmod +x order2
./order2
- flag{N2YyN2ZmZmE2OTEwMGUyYmNhOWRkYTQzOTBhY2IyZmE=}

#### Rebel Intercept
=> nc -lvp 1337 -s 127.0.0.1
- flag{U29tZXRoaW5nLCBTb21ldGhpbmcsIFNvbWV0aGluZywgRGFyayBTaWRl}

#### Trash Talk
C-3PO: Are you there, sir?
Luke: 3PO!
C-3PO: We've had some problems...
Luke: Will you shut up and listen to me? Shut down all garbage mashers on the detention level, will you? Do you copy? Shut down all the garbag
e mashers on the detention level!
- flag{MmY0ODYw}



### A Christmas Catastrophe
#### The Grotto:
- flag{YmRmMDk0}

#### Present Pandemonium
=> jq -s '.[1337]' presents.json
- flag{QW50b25pbw==}
- flag{SmVyc2V5}
- flag{MTYy}
- flag{MC4zMQ==}
- flag{OTk5OS45MQ==}
- flag{YjZjMTVm}


#### Santa's Sleighdar
- flag{OWQzZmM1}

#### Elf in a Shell(f)
- flag{OWRhNWE2}

#### Let It Snow
- not solved

#### Santa's Naughty List
- flag{bmFtZXM=}
- flag{MTMzNA==}
- flag{MjY2Ng==}
- flag{MGEzZGEw}
- flag{MjA5Ng==}
- flag{MjE2Mw==}

#### A Christmas Phish
- flag{ODRkOTNybjFuajRAZ2VuZXJpY2VsZm1haWwub3Jn}
- flag{bmV3c0BuYXRpb25hbGVsZndvcmtlcnN1bmlvbi5jaHJpc3RtYXM=}
- flag{VG05MGFHbHVaeUIwYnlCelpXVWdhR1Z5WlEub25pb24=}
- flag{RnJlZGR5IE1jRmx1ZmY=}

#### A Letter to Santa
http://10.102.188.182/letter.php?message=%3C!--%23exec+cmd%3D%22cat+/etc/user.txt%22+--%3E
- flag{YmFhYjZh}

#### Kringle Inc.
- flag{THVtcCBvZiBjb2Fs}
- flag{SGFycnkgJiBNYXJ2}
- flag{RWdn}


### Kate's Story
#### Kate's Story: Ep.1
- flag{MTQvMDcvMjAxOCAxMzowMDowMw==}
- flag{Q2Fub24gRU9TIDZE}
- flag{U2FsbHkgTWljaGFlbHM=}
- flag{NTHDgsKwIDI2JyAzNi45IiBOb3J0aCwgMsOCwrAgMzgnIDE3LjMiIFdlc3Q=}
- flag{QXNodG9uIENvdXJ0}
- flag{MTkvMDMvMjAxOQ==}
- flag{MTA6NTE6MDQ=}
- flag{QSBjYXIgd2luZG93}

#### Kate's Story: Ep.2
- flag{eG1s}
- flag{MjU2}
- flag{cHlkb2MucHk=}
- flag{MDZjMTY0}

#### Kate's Story: Ep.3
- flag{QmFja2dyb3VuZCBjaGFuZ2VzLCBmaWxlcyBkZWxldGVkLCBwb3B1cCBib3ggYXBwZWFycw==}
- flag{UG93ZXJTaGVsbA==}
- flag{V2FsbHBhcGVy}
- flag{YS5wczE=}

#### Kate's Story: Ep.4
- flag{MHgxMDYw}
- flag{NDY2Mw==}
- flag{cG93ZXJzaGVsbC5leGU=}
- flag{NToyMjowMQ==}
- flag{NTQ=}
- flag{b3V0bG9vay5leGU=}
- flag{NDkxNg==}
- flag{QzpcXFVzZXJzXFxJTUxVc2VyXFxhLnBzMQ==}
- flag{MTcyLjE2LjEwMS4xNDU=}
- flag{RlRQ}
- flag{ZGF2ZTEyMw==}
- flag{TWljaGVsbGUvRGVza3RvcA==}
- flag{cGFzc3dvcmRzLnR4dA==}
- flag{SUxvdmVNeUtpZHMxMjM=}
- flag{aGFja2VyLmV4ZQ==}
- flag{MTE6NTk6NTM=}


### Omnipotent Productions
#### Omnipotent Productions: Ep.1 – Log Analysis
- flag{QSBwb3J0IHNjYW4=}
- flag{MjE=}
- flag{RlRQ}
- flag{My4wLjM=}
- flag{cm9vdA==}

#### Omnipotent Productions: Ep.2 – FTP Server Hardening
- flag{ZDUyYmRk}

=> sudo -l
=> sudo chmod 750 /home/*/
- flag{NWU1NjMw}

#### Omnipotent Productions: Ep.3 – OSINT
- flag{cnVzc2VsamFja19MMzN0}
- flag{QnJpc3RvbA==}
- flag{MjMvMDc=}
- flag{NjE3MQ==}
- flag{MQ==}
- flag{QWxleCBTbGF0ZXI=}

#### Omnipotent Productions: Ep.4 – Packet Analysis
- flag{MTcyLjE3LjAuMw==}
- flag{VHJ1ZQ==}
- flag{U2FtLkI=}
- flag{RlRQLURBVEE=}
- flag{MjAyMS0wNy0yNyAxNzoyOTowNQ==}
- flag{ZFIwcmFuRzM=}

#### Omnipotent Productions: Ep.5 – Forensics
- flag{SW52b2ljZQ==}
- flag{MjAyMS0wNy0zMCAxMDoxNzoxMw==}
- flag{QmFzZTY0}
- flag{VVhCOWFoQ1I=}
- flag{YWxleC5zbGF0ZXIub21uaXBvdGVudHByb2R1Y3Rpb25zQG91dGxvb2suY29t}
- flag{TGVnaW9uT2ZDaGFvczdAb3V0bG9vay5jb20=}
- flag{MC4x}
- flag{M2FhYTg=}

#### Omnipotent Productions: Ep.6 – Theory
- not solved