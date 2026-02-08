import argparse
import logging
from pathlib import Path

from .config import load_config
from .filesystem import secure_filesystem
from .firewall import configure_firewall
from .runner import run_cmd
from .services import disable_services
from .ssh import harden_ssh
from .system import get_linux_distro
from .usb import disable_usb


def setup_logging():
    repo_root = Path(__file__).resolve().parents[2]
    log_file = repo_root / "harden.log"
    logging.basicConfig(
        filename=str(log_file),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def main():
    parser = argparse.ArgumentParser(description="Linux Hardening Tool")
    parser.add_argument("--config", help="Path to config.json")
    parser.add_argument("--dry-run", action="store_true", help="Print commands without executing")
    parser.add_argument("--firewall", action="store_true", help="Enable and configure the firewall")
    parser.add_argument("--disable-services", action="store_true", help="Disable unnecessary services")
    parser.add_argument("--secure-fs", action="store_true", help="Harden filesystem security")
    parser.add_argument("--harden-ssh", action="store_true", help="Secure SSH configuration")
    parser.add_argument("--disable-usb", action="store_true", help="Disable USB storage access")
    parser.add_argument("--all", action="store_true", help="Run all security hardening tasks")

    args = parser.parse_args()
    setup_logging()

    try:
        config = load_config(args.config)
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        raise SystemExit(1) from exc

    linux_system, distro_name = get_linux_distro()
    print(f"Detected OS: {linux_system}, Distro: {distro_name}")

    def _run(cmd):
        return run_cmd(cmd, dry_run=args.dry_run, check=True)

    if not any(vars(args).values()):
        print("[*] No arguments provided. Running all security tasks by default...\n")
        args.all = True

    if args.all:
        configure_firewall(distro_name, config, _run)
        disable_services(config, _run)
        secure_filesystem(config, _run)
        harden_ssh(distro_name, config, _run)
        disable_usb(distro_name, _run)
    elif args.firewall:
        configure_firewall(distro_name, config, _run)
    elif args.disable_services:
        disable_services(config, _run)
    elif args.secure_fs:
        secure_filesystem(config, _run)
    elif args.harden_ssh:
        harden_ssh(distro_name, config, _run)
    elif args.disable_usb:
        disable_usb(distro_name, _run)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
