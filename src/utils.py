import json
import logging
import os

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Путь к папке data
data_dir = os.path.join(current_dir, "..", "data")

# Создаем путь до файла логов относительно текущей директории
log_dir = os.path.join(current_dir, "../logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

rel_file_path = os.path.join(log_dir, "utils.log")
abs_file_path = os.path.abspath(rel_file_path)


# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Создаем обработчик для записи логов в файл
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Создаем форматтер и добавляем его в обработчик
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)


def read_json_file(file_path):
    """Принимает путь к JSON-файлу в качестве аргумента и возвращает
    список словарей с данными о финансовых транзакциях"""
    logger.debug("Получаем данные из файла")
    if not os.path.exists(file_path):
        logger.error("Файл не найден: %s", file_path)
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Данные успешно загружены из файла")
                return data
            logger.warning("Данные в файле не являются списком")
            return []
        except json.JSONDecodeError:
            logger.error("Ошибка декодирования JSON")
            return []
        except Exception as e:
            logger.error("Произошла ошибка: %s", e)
            return []


if __name__ == "__main__":
    transactions = read_json_file(os.path.join(data_dir, "operations.json"))
    print(transactions)
