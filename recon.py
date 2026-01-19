#!/usr/bin/env python3

import os
import sys

import subprocess

try:
    target = sys.argv[1]
    if not os.path.exists(target):
        os.makedirs(target)
        with open(f"{target}/info.txt", "w") as fp:
            fp.write(f"Target initialized: {target}")
            pass
        #print(os.system(f"ping -c 2 {target}"))

        #os.system(f"ping -c 2 {target}")
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
except IndexError:
    print(f"Usage:\n./caseCreator.py <target>")
except subprocess.CalledProcessError:
    print(f"Unknown host '{target}'\ncheck your input")
