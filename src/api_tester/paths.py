from pathlib import Path

# Project root: .../api_tester (parent of src/)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = PROJECT_ROOT / "config"
ENV_FILE = CONFIG_DIR / ".env"
PARAMS_DIR = PROJECT_ROOT / "params"
