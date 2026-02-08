# Linux Hardener

A lightweight Linux hardening toolkit that applies common security controls from a single CLI. It targets firewall setup, service hardening, SSH configuration, USB storage lockdown, and basic file protection.

## Features
- Firewall configuration for UFW (Debian/Ubuntu/Kali) and firewalld (Fedora/CentOS/RHEL)
- Disable unnecessary services defined in config
- SSH hardening (root login and port)
- Optional USB storage disablement
- Filesystem protection for specified files
- Dry-run mode to preview changes

## Supported Distros
- Ubuntu, Debian, Kali, Linux Mint, Pop!_OS
- Fedora, CentOS, RHEL, Rocky, AlmaLinux, Oracle Linux

## Install
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Configuration
Copy the example config and edit it:
```bash
cp config.example.json config.json
```

## Usage
Run all tasks (default):
```bash
sudo linux-hardener
```

Run a single task:
```bash
sudo linux-hardener --harden-ssh
```

Dry-run (no changes applied):
```bash
linux-hardener --all --dry-run
```

## Notes
- SSH changes can lock you out if the new port is not allowed through the firewall.
- `chattr +i` makes files immutable; remove immutability before editing.
