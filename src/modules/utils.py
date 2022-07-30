import json
from datetime import date

def get_current_date() -> str:
    return date.today().strftime("%d.%m.%Y")

def print_json(json_parsed: dict) -> None:
    print(json.dumps(json_parsed))
