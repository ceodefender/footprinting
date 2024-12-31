import os
import subprocess
import pyfiglet
from tqdm import tqdm
from termcolor import colored
import shodan

# Banner
os.system('clear')
banner = pyfiglet.figlet_format("CEO FootPrinTinG TooL")
print(colored(banner, 'cyan'))
print(colored("Author: CEO", 'green'))
print(colored("GitHub: https://github.com/ceotools/footprinting", 'green'))
print("=" * 50)

# Input domain
domain = input(colored("\nEnter your domain: ", 'yellow'))

# Input Shodan API key
shodan_api_key = input(colored("\nEnter your Shodan API key: ", 'yellow')).strip()

# Functions for tools
def run_whois():
    print(colored("\nRunning WHOIS...", 'blue'))
    try:
        subprocess.run(["sudo", "whois", domain], check=True)
        print(colored("\nAdvanced Syntax: sudo whois -h whois.iana.org", 'green'))
    except subprocess.CalledProcessError:
        print(colored("[Error] WHOIS command failed.", 'red'))

def run_traceroute():
    print(colored("\nRunning Traceroute...", 'blue'))
    try:
        subprocess.run(["sudo", "traceroute", domain], check=True)
        print(colored("\nAdvanced Syntax: sudo traceroute -n -T -p 80", 'green'))
    except subprocess.CalledProcessError:
        print(colored("[Error] Traceroute command failed.", 'red'))

def run_dig():
    print(colored("\nRunning DIG...", 'blue'))
    try:
        subprocess.run(["sudo", "dig", "+trace", "+nocmd", domain], check=True)
        print(colored("\nAdvanced Syntax: sudo dig ANY +noall +answer", 'green'))
    except subprocess.CalledProcessError:
        print(colored("[Error] DIG command failed.", 'red'))

def run_nslookup():
    print(colored("\nRunning NSLOOKUP...", 'blue'))
    try:
        subprocess.run(["sudo", "nslookup", "-type=ANY", domain], check=True)
        print(colored("\nAdvanced Syntax: sudo nslookup -type=MX", 'green'))
    except subprocess.CalledProcessError:
        print(colored("[Error] NSLOOKUP command failed.", 'red'))

def run_shodan():
    print(colored("\nRunning Shodan...", 'blue'))
    try:
        api = shodan.Shodan(shodan_api_key)
        host = api.host(domain)
        print(colored(f"\nShodan Results for {domain}:\n", 'green'))
        print(colored(host, 'cyan'))
        print(colored("\nAdvanced Syntax: Use specific Shodan queries like 'port:22'", 'green'))
    except shodan.APIError as e:
        print(colored(f"\n[Error] Shodan API: {e}", 'red'))
    except Exception as e:
        print(colored(f"[Unexpected Error] {e}", 'red'))

def check_firewall():
    print(colored("\nChecking for Firewall...", 'blue'))
    try:
        subprocess.run(["sudo", "nmap", "-p80,443", "-sV", "--script", "http-waf-detect", domain], check=True)
        print(colored("\nAdvanced Syntax: sudo nmap --script=http-waf-detect,http-waf-fingerprint", 'green'))
    except subprocess.CalledProcessError:
        print(colored("[Error] Firewall check failed.", 'red'))

def run_amass():
    print(colored("\nRunning Amass...", 'blue'))
    try:
        subprocess.run(["sudo", "amass", "enum", "-d", domain, "-v"], check=True)
        print(colored("\nAdvanced Syntax: sudo amass enum --passive", 'green'))
    except subprocess.CalledProcessError:
        print(colored("[Error] Amass command failed.", 'red'))

def run_photon():
    print(colored("\nRunning Photon...", 'blue'))
    try:
        subprocess.run(["sudo", "photon", "-u", domain, "-l", "3"], check=True)
        print(colored("\nAdvanced Syntax: sudo photon -u https://example.com -o /output", 'green'))
    except subprocess.CalledProcessError:
        print(colored("[Error] Photon command failed.", 'red'))

# Validate Shodan API key
def validate_shodan_key():
    print(colored("\nValidating Shodan API key...", 'blue'))
    try:
        api = shodan.Shodan(shodan_api_key)
        api.info()
        print(colored("[+] Shodan API key is valid.", 'green'))
        return True
    except shodan.APIError as e:
        print(colored(f"[Error] Invalid Shodan API key: {e}", 'red'))
        return False

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

shodan_valid = validate_shodan_key()

if shodan_valid:
    steps.insert(4, ("Shodan", run_shodan))  # Add Shodan step if the key is valid

for step, function in tqdm(steps, desc="Processing Steps"):
    print(colored(f"\n[+] Executing: {step}", 'yellow'))
    function()
    print(colored(f"\n[+] {step} Completed.\n", 'green'))

print(colored("\nAll tasks completed successfully!", 'cyan'))
