import json
import os

import pandas as pd

from src.masks import get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.search_transactions import search_transactions, sort_transactions
from src.widjet import get_date


def get_operations(data_dir: str) -> list[dict]:
    """Функция для загрузки операций из всех файлов в директории data."""
    transactions = []

    # Загрузка JSON-файла
    json_file_path = os.path.join(data_dir, "operations.json")
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            transactions.extend(json.load(json_file))

    # Загрузка CSV-файла
    csv_file_path = os.path.join(data_dir, "operations.csv")
    if os.path.exists(csv_file_path):
        csv_data = pd.read_csv(csv_file_path)
        transactions.extend(csv_data.to_dict(orient='records'))

    # Загрузка XLSX-файла
    xlsx_file_path = os.path.join(data_dir, "operations.xlsx")
    if os.path.exists(xlsx_file_path):
        xlsx_data = pd.read_excel(xlsx_file_path)
        transactions.extend(xlsx_data.to_dict(orient='records'))

    return transactions


def get_user_input(prompt: str, valid_options: list) -> str:
    """Функция для получения корректного ввода от пользователя."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print("Некорректный выбор. Попробуй еще раз.")


def main() -> None:
    """Основная функция программы."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбор типа файла для загрузки
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = get_user_input("Введите номер пункта меню (1-3):\n", ["1", "2", "3"])

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        data_directory = os.path.join(os.path.dirname(__file__), "../data")
        list_transactions = get_operations(data_directory)
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        data_directory = os.path.join(os.path.dirname(__file__), "../data")
        list_transactions = get_operations(data_directory)
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        data_directory = os.path.join(os.path.dirname(__file__), "../data")
        list_transactions = get_operations(data_directory)

    filters = {}
    filters["status"] = get_user_input(
        "Введите статус для фильтрации (EXECUTED, CANCELED, PENDING):\n",
        ["executed", "canceled", "pending"]
    ).upper()

    if get_user_input("Отсортировать операции по дате? (да/нет)\n", ["да", "нет"]) == "да":
        filters["date"] = get_user_input(
            "Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию)\n",
            ["по возрастанию", "по убыванию"]
        ) == "по убыванию"

    if get_user_input("Выводить только рублевые транзакции? (да/нет)\n", ["да", "нет"]) == "да":
        filters["currency"] = "RUB"

    if get_user_input("Отфильтровать список транзакций по слову в описании? (да/нет)\n", ["да", "нет"]) == "да":
        search = input("Введите слово для поиска: ")
        filtered_transactions = search_transactions(list_transactions, search)
    else:
        filtered_transactions = list_transactions

    # Применение фильтров
    transactions = filtered_transactions
    for filter_type, filter_value in filters.items():
        if filter_type == "status":
            transactions = filter_by_state(transactions, filter_value)
        elif filter_type == "date":
            transactions = sort_by_date(transactions, filter_value)
        elif filter_type == "currency":
            transactions = [txn for txn in transactions if
                            txn.get("operationAmount", {}).get("currency", {}).get("code") == filter_value]

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transactions)}")
    for transaction in transactions:
        description = transaction.get("description")
        from_ = get_mask_card_number(transaction.get("from")) if description != "Открытие вклада" else description
        to_ = get_mask_card_number(transaction.get("to"))
        date = get_date(transaction.get("date"))
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["name"]

        if description == "Открытие вклада":
            print(f"{date} {description}\nСчет {to_}\nСумма: {amount} {currency}\n")
        else:
            print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")

    # Подсчет транзакций по категориям
    categories_operations = [
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод с карты на счет",
        "Перевод со счета на счет",
        "Открытие вклада",
    ]

    if get_user_input("Хотите подсчитать транзакции по категориям? (да/нет)\n", ["да", "нет"]) == "да":
        category_counts = sort_transactions(transactions, categories_operations)
        print("Подсчет транзакций по категориям:")
        for category, count in category_counts.items():
            print(f"{category}: {count} транзакций")


if __name__ == "__main__":
    main()
