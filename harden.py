import os
import json
import logging
import platform
import argparse
import distro  # Import distro module for Linux distribution detection

# Setup logging
log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "harden.log")
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get the absolute path of config.json
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

# Function to load configuration
def load_config():
    if not os.path.exists(config_path):
        logging.error(f"Configuration file not found at {config_path}")
        print("Error: Configuration file not found.")
        exit(1)

    with open(config_path, "r") as file:
        return json.load(file)

config = load_config()

# Detect Linux Distribution
def get_linux_distro():
    return platform.system(), distro.id().lower()

linux_system, distro_name = get_linux_distro()
print(f"Detected OS: {linux_system}, Distro: {distro_name}")

# Security functions
def configure_firewall():
    print("[+] Configuring Firewall...")
    if distro_name in ["ubuntu", "debian", "kali"]:
        os.system("sudo ufw enable")
        os.system(f"sudo ufw default {config['firewall']['default_policy']}")
        for port in config["firewall"]["allow_ports"]:
            os.system(f"sudo ufw allow {port}")
    elif distro_name in ["centos", "fedora"]:
        os.system("sudo systemctl start firewalld")
        os.system("sudo firewall-cmd --set-default-zone=drop")
    logging.info("Firewall configured successfully.")

def disable_services():
    print("[+] Disabling Unnecessary Services...")
    for service in config["services"]["disable"]:
        os.system(f"sudo systemctl stop {service}")
        os.system(f"sudo systemctl disable {service}")
        logging.info(f"Disabled service: {service}")

def secure_filesystem():
    print("[+] Securing File System...")
    for file in config["filesystem"]["protect_files"]:
        os.system(f"sudo chmod 600 {file}")
        os.system(f"sudo chattr +i {file}")
        logging.info(f"Secured file: {file}")

def harden_ssh():
    print("[+] Hardening SSH...")
    os.system("sudo sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config")
    os.system("sudo sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config")
    os.system("sudo systemctl restart sshd")
    logging.info("SSH hardened: Root login disabled, Port changed.")

def disable_usb():
    print("[+] Disabling USB Ports...")
    os.system("echo 'blacklist usb-storage' | sudo tee /etc/modprobe.d/usb-storage.conf")
    os.system("sudo update-initramfs -u")
    logging.info("USB storage disabled.")

# Argument Parsing (for CLI)
def main():
    parser = argparse.ArgumentParser(description="Linux Hardening Tool")
    parser.add_argument("--firewall", action="store_true", help="Enable and configure the firewall")
    parser.add_argument("--disable-services", action="store_true", help="Disable unnecessary services")
    parser.add_argument("--secure-fs", action="store_true", help="Harden filesystem security")
    parser.add_argument("--harden-ssh", action="store_true", help="Secure SSH configuration")
    parser.add_argument("--disable-usb", action="store_true", help="Disable USB storage access")
    parser.add_argument("--all", action="store_true", help="Run all security hardening tasks")

    args = parser.parse_args()

    # Auto-run all tasks if no arguments are provided
    if not any(vars(args).values()):  # Checks if no arguments were given
        print("[*] No arguments provided. Running all security tasks by default...\n")
        args.all = True

    # Execute based on arguments
    if args.all:
        configure_firewall()
        disable_services()
        secure_filesystem()
        harden_ssh()
        disable_usb()
    elif args.firewall:
        configure_firewall()
    elif args.disable_services:
        disable_services()
    elif args.secure_fs:
        secure_filesystem()
    elif args.harden_ssh:
        harden_ssh()
    elif args.disable_usb:
        disable_usb()
    else:
        parser.print_help()

# Ensure script runs only if executed directly
if __name__ == "__main__":
    main()
