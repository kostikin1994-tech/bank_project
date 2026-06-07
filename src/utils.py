import json
import os

def read_json_file(file_path):
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, Exception):
        return []

if __name__ == "__main__":
    from src.utils import read_json_file
    transactions = read_json_file("data/operations.json")
    print(len(transactions))
