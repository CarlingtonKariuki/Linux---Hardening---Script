import logging
import subprocess


def run_cmd(cmd: list[str], dry_run: bool = False, check: bool = True):
    if dry_run:
        logging.info("DRY-RUN: %s", " ".join(cmd))
        print(f"[dry-run] {' '.join(cmd)}")
        return None
    logging.info("RUN: %s", " ".join(cmd))
    return subprocess.run(cmd, check=check)
