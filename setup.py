from setuptools import setup, find_packages

setup(
    name="linux_hardener",
    version="1.1.0",
    description="Linux system hardening toolkit",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=["distro>=1.8"],
    entry_points={
        "console_scripts": [
            "linux-hardener=linux_hardener.cli:main",
            "harden=linux_hardener.cli:main",
        ]
    },
)
