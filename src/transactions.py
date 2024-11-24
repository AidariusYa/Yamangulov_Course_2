import csv
import logging
import os

import pandas as pd


# Получаем путь к директории проекта
current_dir = os.path.dirname(os.path.abspath(__file__))

# Путь к папке data
data_dir = os.path.join(current_dir, "..", "data")

# Пример чтения файла
csv_file_path = os.path.join(data_dir, "transactions.csv")
xlsx_file_path = os.path.join(data_dir, "transactions_excel.xlsx")


# Создаем путь до файла логов относительно текущей директории
log_dir = os.path.join(current_dir, "../logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

rel_file_path = os.path.join(log_dir, "transactions.log")
abs_file_path = os.path.abspath(rel_file_path)

# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("transactions")
logger.setLevel(logging.DEBUG)

# Создаем обработчик для записи логов в файл
file_handler = logging.FileHandler(abs_file_path, "a", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Создаем форматтер и добавляем его в обработчик
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)


def read_transactions_from_csv(file_path):
    """Считывает финансовые операции из CSV файла.

    :param file_path: Путь к файлу CSV.
    :return: Список словарей с транзакциями.
    """
    transactions = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transactions.append(row)
        logger.info(f"Успешно считано {len(transactions)} транзакций из {file_path}.")
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
    return transactions


def read_transactions_from_excel(file_path):
    """Считывает финансовые операции из Excel файла.

    :param file_path: Путь к файлу Excel.
    :return: Список словарей с транзакциями.
    """
    transactions = []
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient='records')
        logger.info(f"Успешно считано {len(transactions)} транзакций из {file_path}.")
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
    return transactions


if __name__ == "__main__":
    transactions_csv = read_transactions_from_csv(csv_file_path)
    transactions_excel = read_transactions_from_excel(xlsx_file_path)
    print(transactions_csv)
    print(transactions_excel)
