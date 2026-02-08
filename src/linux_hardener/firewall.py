from .system import is_debian_like, is_rhel_like


def configure_firewall(distro_name: str, config: dict, run_cmd):
    print("[+] Configuring Firewall...")
    firewall_cfg = config.get("firewall", {})
    allow_ports = firewall_cfg.get("allow_ports", [])
    default_policy = firewall_cfg.get("default_policy", "deny")

    if is_debian_like(distro_name):
        run_cmd(["sudo", "ufw", "default", str(default_policy)])
        for port in allow_ports:
            run_cmd(["sudo", "ufw", "allow", str(port)])
        run_cmd(["sudo", "ufw", "enable"])
    elif is_rhel_like(distro_name):
        run_cmd(["sudo", "systemctl", "enable", "--now", "firewalld"])
        run_cmd(["sudo", "firewall-cmd", "--set-default-zone=drop"])
        for port in allow_ports:
            run_cmd(["sudo", "firewall-cmd", "--permanent", "--add-port", f"{port}/tcp"])
        run_cmd(["sudo", "firewall-cmd", "--reload"])
    else:
        print(f"[!] Unsupported distro for firewall config: {distro_name}")
