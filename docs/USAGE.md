# Usage Guide

## Quick Start
```bash
cp config.example.json config.json
sudo linux-hardener
```

## Dry Run
Preview commands without applying changes:
```bash
linux-hardener --all --dry-run
```

## Task-specific Runs
```bash
sudo linux-hardener --firewall
sudo linux-hardener --harden-ssh
sudo linux-hardener --disable-usb
```

## SSH Safety
If you change the SSH port, ensure the firewall allows that port before restarting SSH.
