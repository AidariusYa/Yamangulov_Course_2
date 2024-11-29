import re
from collections import Counter


def search_transactions(file: list[dict], input_user: str) -> list[dict]:
    """Функция, которая принимает список словарей с информацией о банковских операциях и строку для поиска,
    и возвращает список словарей, содержащих эту строку в описании."""
    new_list = []
    for i in file:
        if 'description' in i and re.findall(input_user, i['description'], re.IGNORECASE):
            new_list.append(i)
    return new_list


def sort_transactions(file: list[dict], category: list) -> dict:
    """Функция, которая создает и возвращает словарь, где ключами являются названия категорий, а значениями —
    количество операций в каждой из этих категорий."""
    new = []
    for j in file:
        if 'description' in j:
            for cat in category:
                if cat in j['description']:
                    new.append(cat)
    return Counter(new)
