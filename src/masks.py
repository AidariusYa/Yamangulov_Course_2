import logging
import os

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Создаем обработчик для записи логов в файл
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Создаем форматтер и добавляем его в обработчик
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Возвращает замаскированный номер банковской карты в формате XXXX XX** **** XXXX"""
    logger.debug("Маскируем карту клиента")
    try:
        if len(card_number) <= 4:
            return card_number  # Возвращает номер без изменений, если он меньше или равен 4 символам
        elif len(card_number) < 6:
            return f"{card_number[:4]}**"  # Если длина 5, показывает 4 и маскирует остальные
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"  # Стандартный вариант
    except Exception as e:
        logger.error("Произошла ошибка: %s", e)
    finally:
        logger.info("Функция выполнена успешно")


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер банковского счета в формате **XXXX"""
    logger.debug("Маскируем счёт клиента")
    try:
        if len(account_number) < 4:  # Возвращает номер без изменений, если он меньше 4 символов
            return account_number
        elif len(account_number) == 4:
            return f"**{account_number[-2:]}"
        return f"**{account_number[-4:]}"
    except Exception as e:
        logger.error("Произошла ошибка: %s", e)
    finally:
        logger.info("Функция выполнена успешно")


if __name__ == "__main__":
    print(get_mask_card_number("1234567890123456"))
    print(get_mask_account("12345678901234567890"))
