import time
import os


def host_enum():
    subnet = input("\nPlease enter target subnet range (ex. 192.168.1.1/24) >> ").strip()
    choice = input("Would you like to grep the results to only see the hosts IPs (y/n): ").strip().lower()
    if choice == "y":
        os.system("clear")
        print(f"\n[>] Starting Host Enumeration on {subnet}...\n")
        os.system(f"sudo nmap -sn {subnet} | grep 'for'")
    elif choice == "n":
        os.system("clear")
        print(f"\n[>] Starting Host Enumeration on {subnet}...\n")
        os.system(f"sudo nmap -sn {subnet}")
    else:
        print("[!] Invalid input, expected y or n")


def service_enum():
    target = input("\nTarget Device IP >> ").strip()
    choice = input("Are you checking a specific port? (y/n): ").strip().lower()
    if choice == "y":
        port = input("Target Port >> ").strip()
        os.system("clear")
        print("\n[>] Starting Service Enumeration...\n")
        os.system(f"sudo nmap -sV -sC -O -p {port} {target}")
    elif choice == "n":
        os.system("clear")
        print("\n[>] Starting Service Enumeration...\n")
        os.system(f"sudo nmap -sV -sC -O {target}")
    else:
        print("[!] Invalid input, expected y or n")


def port_enum():
    target = input("\nTarget Device IP >> ").strip()
    os.system("clear")
    print("\n[>] Starting TCP Scan...\n")
    os.system(f"sudo nmap -sS -Pn {target}")

def check_ip():
    print("[*] Getting Your IP...")
    time.sleep(2)
    os.system("ip a | grep 'inet '")

def exit_program():
    print("\n[!] Exiting the program....\n")
    time.sleep(2)

# program loop
while True:
    print("")
    print(">> Nmap Scanning Tool by Logz00 <<")
    print("")
    print("[>] Scan Options ")
    print("")
    print("[1] LAN Host Enumeration")
    print("[2] TCP Port Scan (open ports)")
    print("[3] Service Enumeration")
    print("[4] Check My IP Info")
    print("[5] Exit")
    print("")

    try:
        scan_type = int(input("Scan Option >>  "))
    except ValueError:
        print("[!] Please enter a number 1-5")
        continue

    if scan_type == 1:
        host_enum()
    elif scan_type == 2:
        port_enum()
    elif scan_type == 3:
        service_enum()
    elif scan_type == 4:
        check_ip()
    elif scan_type == 5:
        exit_program()
        break
    else:
        os.system("clear")
        print("[!] Invalid option, expected an option 1-5")





