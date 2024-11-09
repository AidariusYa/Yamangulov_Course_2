import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


def test_filter_by_currency(transactions):
    """Тестирование фильтрации по валюте"""
    usd_transactions = list(filter_by_currency(transactions, "USD"))

    # Проверяем, что количество USD транзакций равно 3
    assert len(usd_transactions) == 3  # Проверяем, что количество USD транзакций равно 3

    # Проверяем, что все транзакции имеют валюту USD
    for transaction in usd_transactions:
        assert transaction['operationAmount']['currency']['code'] == "USD"

    # Проверяем, что функция возвращает пустой список для валюты, которой нет
    eur_transactions = list(filter_by_currency(transactions, "EUR"))

    # Должен вернуть пустой список
    assert len(eur_transactions) == 0

    # Проверяем, что функция не выдает ошибку при обработке пустого списка
    empty_transactions = []
    empty_result = list(filter_by_currency(empty_transactions, "USD"))

    # Должен вернуть пустой список
    assert empty_result == []


def test_transaction_descriptions(transactions):
    """Тест для получения описания транзакций"""
    descriptions = list(transaction_descriptions(transactions))

    # Проверяем, что количество описаний соответствует количеству транзакций
    assert len(descriptions) == len(transactions)

    # Проверяем, что описания соответствуют ожидаемым
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]
    assert descriptions == expected_descriptions

    # Проверяем, что функция не выдает ошибку при обработке пустого списка
    empty_descriptions = list(transaction_descriptions([]))

    # Должен вернуть пустой список
    assert empty_descriptions == []


def test_card_number_generator():
    """Тест для генерации номеров карт от 1 до 5"""
    generated_numbers = list(card_number_generator(1, 5))
    expected_numbers = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]
    assert generated_numbers == expected_numbers

    # Проверяем, что генератор корректно обрабатывает крайние значения диапазона
    single_number = list(card_number_generator(1, 1))
    assert single_number == ["0000 0000 0000 0001"]

    # Проверяем, что генератор не выдает ошибку при пустом диапазоне
    empty_range = list(card_number_generator(5, 1))

    # Должен вернуть пустой список
    assert empty_range == []
