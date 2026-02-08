import json
import logging
from pathlib import Path

DEFAULT_CONFIG_NAME = "config.json"
EXAMPLE_CONFIG_NAME = "config.example.json"


def get_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def get_default_config_path() -> Path:
    return get_repo_root() / DEFAULT_CONFIG_NAME


def load_config(path: str | None = None) -> dict:
    config_path = Path(path) if path else get_default_config_path()
    if not config_path.exists():
        example = get_repo_root() / EXAMPLE_CONFIG_NAME
        msg = (
            f"Configuration file not found at {config_path}. "
            f"Copy {example.name} to {DEFAULT_CONFIG_NAME} and edit it."
        )
        logging.error(msg)
        raise FileNotFoundError(msg)
    with config_path.open("r", encoding="utf-8") as file:
        return json.load(file)
