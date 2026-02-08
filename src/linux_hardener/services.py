
def disable_services(config: dict, run_cmd):
    print("[+] Disabling Unnecessary Services...")
    for service in config.get("services", {}).get("disable", []):
        run_cmd(["sudo", "systemctl", "stop", service])
        run_cmd(["sudo", "systemctl", "disable", service])
