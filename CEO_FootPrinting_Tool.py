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
    subprocess.run(["whois", domain])


def run_traceroute():
    print(colored("\nRunning Traceroute...", 'blue'))
    subprocess.run(["traceroute", domain])


def run_dig():
    print(colored("\nRunning DIG...", 'blue'))
    subprocess.run(["dig", "+trace", "+nocmd", domain])


def run_nslookup():
    print(colored("\nRunning NSLOOKUP...", 'blue'))
    subprocess.run(["nslookup", "-type=ANY", domain])


def run_shodan():
    print(colored("\nRunning Shodan...", 'blue'))
    try:
        api = shodan.Shodan(shodan_api_key)
        host = api.host(domain)
        print(colored(f"\nShodan Results for {domain}:\n", 'green'))
        print(colored(host, 'cyan'))
    except shodan.APIError as e:
        print(colored(f"\nShodan Error: {e}", 'red'))


def check_firewall():
    print(colored("\nChecking for Firewall...", 'blue'))
    subprocess.run(["nmap", "-p80,443", "-sV", "--script", "http-waf-detect", domain])


def run_amass():
    print(colored("\nRunning Amass...", 'blue'))
    subprocess.run(["amass", "enum", "-d", domain, "-v"])


def run_photon():
    print(colored("\nRunning Photon...", 'blue'))
    subprocess.run(["photon", "-u", domain, "-l", "3"])

# Progress bar for execution
steps = [
    ("WHOIS", run_whois),
    ("Traceroute", run_traceroute),
    ("DIG", run_dig),
    ("NSLOOKUP", run_nslookup),
    ("Shodan", run_shodan),
    ("Firewall Check", check_firewall),
    ("Amass", run_amass),
    ("Photon", run_photon)
]

for step, function in tqdm(steps, desc="Processing Steps"):
    print(colored(f"\n[+] Executing: {step}", 'yellow'))
    function()
    print(colored(f"\n[+] {step} Completed.\n", 'green'))

print(colored("\nAll tasks completed successfully!", 'cyan'))
