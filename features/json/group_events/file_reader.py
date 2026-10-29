import json
from pathlib import Path

def load_events():
    file_path = Path(__file__).with_name("events.json")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)