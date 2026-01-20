# recon-python

Network reconnaissance tool for domains/IPs.
Automates `ping` and `nmap` scans based on user privileges.

## Features
- **Basic Scan:** Ping + Standard Nmap.
- **Root Scan:** Detecting OS (`-O`) and Service Version (`-sV`) automatically if run with `sudo`.

## Installation

```bash
git clone [https://github.com/Zzezlik/recon-python.git](https://github.com/Zzezlik/recon-python.git)
cd recon-python
chmod +x recon.py
```
Usage

Default Scan:
```Bash
./recon.py <target>
```
Advanced Scan (Root):
```Bash
sudo ./recon.py <target>
```
Created by Ath
