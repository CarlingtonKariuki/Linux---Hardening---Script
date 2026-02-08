# Configuration Reference

Example `config.json` structure:
```json
{
  "firewall": {
    "default_policy": "deny",
    "allow_ports": [22, 80, 443]
  },
  "services": {
    "disable": ["avahi-daemon", "cups", "rpcbind"]
  },
  "filesystem": {
    "protect_files": ["/etc/passwd", "/etc/shadow"]
  },
  "ssh": {
    "port": 2222,
    "permit_root_login": false
  }
}
```

Notes:
- `ssh.port` changes the SSH listening port.
- `filesystem.protect_files` are set to `chmod 600` and `chattr +i`.
