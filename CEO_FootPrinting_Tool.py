import os
import subprocess
import pyfiglet
from tqdm import tqdm
from termcolor import colored

# Banner
os.system('clear')
banner = pyfiglet.figlet_format("CEO FootPrinTinG TooL")
print(colored(banner, 'cyan'))
print(colored("Author: CEO", 'green'))
print(colored("GitHub: https://github.com/ceotools/footprinting", 'green'))
print("=" * 50)

# Input domain
domain = input(colored("\nEnter your domain: ", 'yellow'))

# Functions for tools
def run_whois():
    print(colored("\nRunning WHOIS...", 'blue'))
    try:
        subprocess.run(["sudo", "whois", domain], check=True)
    except subprocess.CalledProcessError:
        print(colored("[Error] WHOIS command failed.", 'red'))

def run_traceroute():
    print(colored("\nRunning Traceroute...", 'blue'))
    try:
        subprocess.run(["sudo", "traceroute", domain], check=True)
    except subprocess.CalledProcessError:
        print(colored("[Error] Traceroute command failed.", 'red'))

def run_dig():
    print(colored("\nRunning DIG...", 'blue'))
    try:
        subprocess.run(["sudo", "dig", "+trace", "+nocmd", domain], check=True)
    except subprocess.CalledProcessError:
        print(colored("[Error] DIG command failed.", 'red'))

def run_nslookup():
    print(colored("\nRunning NSLOOKUP...", 'blue'))
    try:
        subprocess.run(["sudo", "nslookup", domain], check=True)
    except subprocess.CalledProcessError:
        print(colored("[Error] NSLOOKUP command failed.", 'red'))

def check_firewall():
    print(colored("\nChecking for Firewall...", 'blue'))
    try:
        subprocess.run(["sudo", "nmap", "-p80,443", "-sV", "--script", "http-waf-detect", domain], check=True)
    except subprocess.CalledProcessError:
        print(colored("[Error] Firewall check failed.", 'red'))

def run_amass():
    print(colored("\nRunning Amass...", 'blue'))
    try:
        subprocess.run(["sudo", "amass", "enum", "-d", domain, "-v"], check=True)
    except subprocess.CalledProcessError:
        print(colored("[Error] Amass command failed.", 'red'))

def run_photon():
    print(colored("\nRunning Photon...", 'blue'))
    try:
        subprocess.run(["sudo", "photon", "-u", domain, "-l", "3"], check=True)
    except subprocess.CalledProcessError:
        print(colored("[Error] Photon command failed.", 'red'))

# Progress bar for execution
steps = [
    ("WHOIS", run_whois),
    ("Traceroute", run_traceroute),
    ("DIG", run_dig),
    ("NSLOOKUP", run_nslookup),
    ("Firewall Check", check_firewall),
    ("Amass", run_amass),
    ("Photon", run_photon)
]

for step, function in tqdm(steps, desc="Processing Steps"):
    print(colored(f"\n[+] Executing: {step}", 'yellow'))
    function()
    print(colored(f"\n[+] {step} Completed.\n", 'green'))

print(colored("\nAll tasks completed successfully!", 'cyan'))
