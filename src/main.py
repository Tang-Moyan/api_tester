"""
Example entry: load config from config/.env, params from params/, demo handler output.
From project root:  python src/main.py
(Requires deps: pip install -e .)
"""

from __future__ import annotations

from pathlib import Path

from api_tester.handlers.result import print_summary, save_json
from api_tester.params_loader import read_json, read_text
from api_tester.paths import PROJECT_ROOT
from api_tester.settings import get_env, load_env


def main() -> None:
    load_env()

    # Demo: load env (no real HTTP call here)
    base_url = get_env("API_BASE_URL", "(not set)")
    print(f"API_BASE_URL from config/.env: {base_url}")

    # Demo: params from subfolders
    prompt_template = read_text("llm/example_prompt.txt").strip()
    query_params = read_json("api/example_query.json")

    record = {
        "label": "demo",
        "status": "ok",
        "meta": {
            "prompt_preview": prompt_template[:80] + "..."
            if len(prompt_template) > 80
            else prompt_template,
            "api_params": query_params,
        },
        "body": {"message": "Replace this with real API response handling."},
    }

    print_summary(record)
    out = save_json(record, PROJECT_ROOT / "output")
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
