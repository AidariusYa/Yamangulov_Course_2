import pytest
import re

from src.search_transactions import search_transactions, sort_transactions
from collections import Counter


transaction_data = [
    {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "SoL",
        "currency_code": "PEN",
        "from": "Счет 58803664651298323391",
        "to": "Счет 39746506635466619397",
        "description": "Перевод организации",
    }
]


def test_search_transactions_found():
    """Проверяет, что функция находит транзакцию по части описания."""
    result = search_transactions(transaction_data, "Перевод")
    assert len(result) == 1
    assert result[0]['id'] == "650703"


def test_search_transactions_not_found():
    """Проверяет, что функция не находит транзакцию, если описание не содержит искомую строку."""
    result = search_transactions(transaction_data, "Не найдено")
    assert len(result) == 0


def test_search_transactions_case_insensitive():
    """Проверяет, что функция работает корректно с учетом регистра"""
    result = search_transactions(transaction_data, "перевод")
    assert len(result) == 1
    assert result[0]['id'] == "650703"


def test_search_transactions_empty_description():
    """Проверяет, что функция не возвращает транзакции с пустым описанием."""
    empty_description_data = [
        {
            "id": "650704",
            "state": "EXECUTED",
            "date": "2023-09-06T11:30:32Z",
            "amount": "5000",
            "currency_name": "SoL",
            "currency_code": "PEN",
            "from": "Счет 58803664651298323391",
            "to": "Счет 39746506635466619397",
            "description": "",
        }
    ]
    result = search_transactions(empty_description_data, "Перевод")
    assert len(result) == 0


def test_search_transactions_multiple_matches():
    """Проверяет, что функция может находить несколько транзакций, соответствующих критериям поиска."""
    multiple_transactions_data = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "SoL",
            "currency_code": "PEN",
            "from": "Счет 58803664651298323391",
            "to": "Счет 39746506635466619397",
            "description": "Перевод организации",
        },
        {
            "id": "650704",
            "state": "EXECUTED",
            "date": "2023-09-06T11:30:32Z",
            "amount": "5000",
            "currency_name": "SoL",
            "currency_code": "PEN",
            "from": "Счет 58803664651298323391",
            "to": "Счет 39746506635466619397",
            "description": "Перевод средств",
        }
    ]
    result = search_transactions(multiple_transactions_data, "Перевод")
    assert len(result) == 2


def test_sort_transactions_single_category_found():
    """Проверяет, что функция правильно подсчитывает количество операций
    для одной категории, которая присутствует в описании."""
    categories = ["Перевод", "Открытие вклада"]
    result = sort_transactions(transaction_data, categories)
    expected = Counter({"Перевод": 1})
    assert result == expected


def test_sort_transactions_multiple_categories_found():
    """Проверяет, что функция правильно подсчитывает количество операций
    для нескольких категорий, которые присутствуют в описаниях."""
    transaction_data_multiple = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "SoL",
            "currency_code": "PEN",
            "from": "Счет 58803664651298323391",
            "to": "Счет 39746506635466619397",
            "description": "Перевод организации",
        },
        {
            "id": "650704",
            "state": "EXECUTED",
            "date": "2023-09-06T11:30:32Z",
            "amount": "5000",
            "currency_name": "SoL",
            "currency_code": "PEN",
            "from": "Счет 58803664651298323391",
            "to": "Счет 39746506635466619397",
            "description": "Оплата услуг",
        }
    ]
    categories = ["Перевод", "Оплата", "Получение"]
    result = sort_transactions(transaction_data_multiple, categories)
    expected = Counter({"Перевод": 1, "Оплата": 1})
    assert result == expected


def test_sort_transactions_no_categories_found():
    """Проверяет, что функция возвращает пустой счетчик,
    если ни одна из категорий не найдена в описаниях."""
    categories = ["Получение", "Возврат"]
    result = sort_transactions(transaction_data, categories)
    expected = Counter()
    assert result == expected


def test_sort_transactions_empty_description():
    """Проверяет, что функция возвращает пустой счетчик,
    если описание транзакции пустое."""
    empty_description_data = [
        {
            "id": "650705",
            "state": "EXECUTED",
            "date": "2023-09-07T11:30:32Z",
            "amount": "3000",
            "currency_name": "SoL",
            "currency_code": "PEN",
            "from": "Счет 58803664651298323391",
            "to": "Счет 39746506635466619397",
            "description": "",
        }
    ]
    categories = ["Перевод", "Оплата"]
    result = sort_transactions(empty_description_data, categories)
    expected = Counter()
    assert result == expected
