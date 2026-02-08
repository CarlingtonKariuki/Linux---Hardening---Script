from .system import is_debian_like, is_rhel_like


def disable_usb(distro_name: str, run_cmd):
    print("[+] Disabling USB Ports...")
    run_cmd([
        "sudo",
        "bash",
        "-c",
        "echo 'blacklist usb-storage' > /etc/modprobe.d/usb-storage.conf",
    ])

    if is_debian_like(distro_name):
        run_cmd(["sudo", "update-initramfs", "-u"])
    elif is_rhel_like(distro_name):
        run_cmd(["sudo", "dracut", "-f"])
    else:
        print(f"[!] Skipping initramfs update for unsupported distro: {distro_name}")
