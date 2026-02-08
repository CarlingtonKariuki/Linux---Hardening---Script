import platform
import distro


def get_linux_distro() -> tuple[str, str]:
    return platform.system(), distro.id().lower()


def is_debian_like(name: str) -> bool:
    return name in ["ubuntu", "debian", "kali", "linuxmint", "pop"]


def is_rhel_like(name: str) -> bool:
    return name in ["centos", "fedora", "rhel", "rocky", "almalinux", "ol"]
