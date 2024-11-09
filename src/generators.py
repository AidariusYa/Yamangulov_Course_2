def filter_by_currency(transactions, currency):
    """Фильтрует транзакции по заданной валюте и возвращает итератор"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Генерирует описания транзакций по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, stop):
    """Генерирует номера банковских карт в заданном диапазоне"""
    for number in range(start, stop + 1):
        yield (f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " +
               f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:16])
