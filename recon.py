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
            fp.write(f"\nTarget initialized: {target}\n")
            pass

        print(f"\n[*] Scanning {target}\n")
        try:
            subprocess.run(["ping", "-c", "2", target], check=True)
            print(f"\n[+] {target} is reachable\n")

        except subprocess.CalledProcessError:
            print(f"\n[-] {target} is not reachable\n")

        try:
            subprocess.run(["nmap", "-T5", "-script=finger,ftp-anon,http-google-malware,http-robots.txt", "-sC", target, "-oN", f"./{target}/nmap-{target}.txt"], check=True)
        except:
            print(f"\n[-] Nmap error\n")
        
    else:
        print(f"\n[!] file already exists\n")
#filter errors if args not given
except IndexError:
    print(f"\nUsage:\n./recon.py <target>\n")
#target is not reachable
except subprocess.CalledProcessError:
    print(f"\nUnknown host '{target}'\nTarget is unreachable\n")
