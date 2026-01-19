#!/usr/bin/env python3

import os
import sys

import subprocess

try:
    #get a first argument ./recon.py <argument-1>
    target = sys.argv[1]

    #check for folder in current directory
    if not os.path.exists(target):
        os.makedirs(target)
        with open(f"{target}/info.txt", "w") as fp:
            fp.write(f"Target initialized: {target}")
            pass

        print(f"[*] Scanning {target}")
        try:
            subprocess.run(["ping", "-c", "2", target], check=True)
            print(f"[+] {target} is reachable")

        except subprocess.CalledProcessError:
            print(f"[-] {target} is not reachable")

        try:
            subprocess.run(["nmap", "-F", target, "-oN", f"nmap-{target}.txt"], check=True)
        except:
            print(f"[-] Nmap error")
        
    else:
        print(f"[!] file already exists")
#filter errors if args not given
except IndexError:
    print(f"Usage:\n./recon.py <target>")
#target is not reachable
except subprocess.CalledProcessError:
    print(f"Unknown host '{target}'\nTarget is unreachable")
