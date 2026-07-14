import json

from pathlib import Path

json_path = Path("data/disease_info.json")

with open(json_path, "r") as f:
    DISEASE_INFO = json.load(f)