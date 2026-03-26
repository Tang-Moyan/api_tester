"""Load test parameters from params/<category>/ files."""

from pathlib import Path
from typing import Any

from api_tester.paths import PARAMS_DIR


def params_subdir(name: str) -> Path:
    return PARAMS_DIR / name


def read_text(relative_under_params: str) -> str:
    path = PARAMS_DIR / relative_under_params
    return path.read_text(encoding="utf-8")


def read_json(relative_under_params: str) -> Any:
    import json

    path = PARAMS_DIR / relative_under_params
    return json.loads(path.read_text(encoding="utf-8"))
