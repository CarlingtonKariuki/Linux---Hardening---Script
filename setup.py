from setuptools import setup

setup(
    name="linux_hardener",  # Package name
    version="1.0",
    py_modules=["harden"],  # Your script file (harden.py)
    install_requires=[],
    entry_points={
        "console_scripts": [
            "harden=harden:main",  # Creates the CLI command 'harden'
        ],
    },
)
