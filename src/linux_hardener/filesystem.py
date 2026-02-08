import logging
import os


def secure_filesystem(config: dict, run_cmd):
    print("[+] Securing File System...")
    for path in config.get("filesystem", {}).get("protect_files", []):
        if not os.path.exists(path):
            logging.warning("File not found for protection: %s", path)
            continue
        run_cmd(["sudo", "chmod", "600", path])
        run_cmd(["sudo", "chattr", "+i", path])
