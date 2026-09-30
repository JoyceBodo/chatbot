
from pathlib import Path
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_config(config_path=None):

    if config_path is None:
        config_path = PROJECT_ROOT / "config" / "config.yaml"

    config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}"
        )

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def get_project_path(config, key):

    relative_path = config["paths"][key]

    return PROJECT_ROOT / relative_path
