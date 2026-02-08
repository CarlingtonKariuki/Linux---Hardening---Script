from .system import is_debian_like


def harden_ssh(distro_name: str, config: dict, run_cmd):
    print("[+] Hardening SSH...")
    ssh_cfg = config.get("ssh", {})
    port = ssh_cfg.get("port", 2222)
    permit_root = ssh_cfg.get("permit_root_login", False)
    permit_root_value = "yes" if permit_root else "no"
    config_path = "/etc/ssh/sshd_config"

    run_cmd([
        "sudo",
        "bash",
        "-c",
        (
            f"grep -qE '^#?PermitRootLogin' {config_path} && "
            f"sed -i -E 's/^#?PermitRootLogin.*/PermitRootLogin {permit_root_value}/' {config_path} "
            f"|| echo 'PermitRootLogin {permit_root_value}' >> {config_path}"
        ),
    ])

    run_cmd([
        "sudo",
        "bash",
        "-c",
        (
            f"grep -qE '^#?Port' {config_path} && "
            f"sed -i -E 's/^#?Port.*/Port {port}/' {config_path} "
            f"|| echo 'Port {port}' >> {config_path}"
        ),
    ])

    service = "ssh" if is_debian_like(distro_name) else "sshd"
    run_cmd(["sudo", "systemctl", "restart", service])
