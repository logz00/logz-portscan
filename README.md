# nmap-tool

A simple Python automated scanner using Nmap for quick network scanning from the command line. Built for personal use, learning, and pent testing.

## What it does

CLI tool that runs nmap scans used for pen testing and network discovery. Makes network scanning fast and easy.

- **Host Enumeration**: ping sweep a subnet to see what's alive on the network
- **TCP Port Scan**: SYN scan to find open ports on a target
- **Service Enumeration**: version detection, default scripts, and OS fingerprinting on a target (with optional single-port mode)
- **IP Check**: quick way to grab your own IP info

## Requirements

- Python
- Nmap installed (`sudo apt install nmap` or `sudo pacman -S nmap`)
- Root/sudo privileges (Nmap needs it for SYN scans and OS detection)

## Usage

```bash
sudo python main.py
# or
sudo python3 main.py
```

Pick a scan option from the menu and follow the prompts.

## Heads up

This is meant for pen testing ONLY on networks you have permission from. Don't use unethically. 

