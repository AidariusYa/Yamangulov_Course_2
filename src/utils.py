import json
import os


def read_json_file(file_path):
    """Принимает путь к JSON-файлу в качестве аргумента и возвращает
    список словарей с данными о финансовых транзакциях"""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
        except json.JSONDecodeError:
            return []


if __name__ == "__main__":
    transactions = read_json_file("data/operations.json")
    print(transactions)
