import os
from pathlib import Path

from dotenv import load_dotenv

from api_tester.paths import ENV_FILE


def load_env(env_path: Path | None = None) -> None:
    path = env_path or ENV_FILE
    if path.is_file():
        load_dotenv(path, override=False)


def get_env(key: str, default: str | None = None) -> str | None:
    return os.environ.get(key, default)
