from datetime import datetime


def mask_account_card(card_info: str) -> str:
    """Функция маскирует номер карты или счета"""
    # Разделение информации на тип и номер
    card_type, card_number = card_info.rsplit(' ', 1)

    if "Count" in card_type:
        # Маскировка для счета
        return f"{card_type} **{card_number[-4:]}"
    else:
        # Маскировка для карт
        return f"{card_type} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


print(mask_account_card("Visa Platinum 7000792289606361"))


def get_date(date_str: str) -> str:
    """Преобразует строку с датой в формат ДД.ММ.ГГГГ."""
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))
