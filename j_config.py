import json
import os

CONFIG_FILE = "assistant_config.json"

DEFAULT_CONFIG = {
    "wake_words": ["harry", "potter", "dev"],
    "last_intent": None,
    "ui_alpha": 0.95
}


def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()

    try:
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)

        # merge defaults (forward compatible)
        for k, v in DEFAULT_CONFIG.items():
            data.setdefault(k, v)

        return data

    except (json.JSONDecodeError, IOError):
        # corrupted file fallback
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()


def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)
