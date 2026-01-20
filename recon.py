#!/usr/bin/env python3

import os
import sys

import subprocess

root = False

if os.getuid() == 0:
    root = True
    print("[!] Running script as root \n(nmap using -sV which guess version of service and os)")
else:
    print("[!] Running script as user")

try:
    #get a first argument ./recon.py <argument-1>
    target = sys.argv[1]

    #check for folder in current directory
    if not os.path.exists(target):
        os.makedirs(target)
        with open(f"{target}/info.txt", "w") as fp:
            fp.write(f"\nTarget initialized: {target}\n")
            subprocess.run(["chmod", "770", f"./{target}/"])
            pass

    else:
        print(f"[-] Folder \"{target}\" already exists")
    try:
        print(f"\n[*] Scanning {target}\n")
        subprocess.run(["ping", "-c", "2", target], check=True)
        print(f"\n[+] {target} is reachable\n")

    except subprocess.CalledProcessError:
            print(f"\n[-] {target} is not reachable\n")

    try:
        if root:
            subprocess.run(["nmap", "-T3", "-script=vuln", "-sC", "-sV", "-osscan-guess", "-O", target, "-oN", f"./{target}/nmap-{target}.txt"], check=True)
        else:
            subprocess.run(["nmap", "-T3", "-script=vuln", "-sC", target, "-oN", f"./{target}/nmap-{target}.txt"], check=True)
    except:
        print(f"\n[-] Nmap error\n")
    
#filter errors if args not given
except IndexError:
    print(f"\nUsage:\n")
    print(f"> ./recon.py <target>")
    print(f"> sudo ./recon.py <target> : use -sV in nmap, for service version and os guess\n")
#target is not reachable
except subprocess.CalledProcessError:
    print(f"\nUnknown host '{target}'\nTarget is unreachable\n")
