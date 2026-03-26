from __future__ import annotations

import json
from abc import ABC, abstractmethod
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class ResultHandler(ABC):
    """Process API responses: normalize, merge with metadata, output."""

    @abstractmethod
    def handle(self, raw: Any, meta: dict[str, Any] | None = None) -> dict[str, Any]:
        """Return a structured record (dict) from raw API result."""


def print_summary(record: dict[str, Any]) -> None:
    label = record.get("label", "result")
    status = record.get("status", "?")
    print(f"[{label}] status={status}")
    body = record.get("body")
    if body is not None:
        if isinstance(body, (dict, list)):
            print(json.dumps(body, ensure_ascii=False, indent=2))
        else:
            print(body)


def save_json(
    record: dict[str, Any],
    out_dir: Path,
    *,
    prefix: str = "api_result",
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    path = out_dir / f"{prefix}_{ts}.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
    return path
