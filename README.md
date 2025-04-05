# 🛡️ Linux Hardener

An automated Linux hardening tool built with Python to help users secure their Linux systems using best practices. It includes firewall configuration, service management, SSH hardening, USB port control, and filesystem protections — all in an interactive or automated CLI.

## 🔐 Features

- 🔥 Configure UFW or iptables firewall
- ❌ Disable unnecessary services
- 🔑 SSH configuration hardening
- 🔌 Optionally disable USB ports
- 📁 File permissions and auditing
- ⚙️ Works on multiple Linux distributions
- 🧠 Interactive CLI prompts for custom setups

## 🚀 How to Use

### 🖥️ Interactive Mode
```bash
sudo python3 hardener.py --interactive

#Automated Mode
#sudo python3 hardener.py --auto --disable-usb --harden-ssh
#Supported Distros
#ubuntu, Debian, Kali linux, CentOS.
#Installation
#Clone the repository:
#git clone https://github.com/YOUR_USERNAME/linux-hardener.git
#cd linux-hardener
#Make the script executable:
#chmod +x hardener.py
#Run the script:
#sudo python3 hardener.py