def get_mask_card_number(card_number: str) -> str:
    """Возвращает замаскированный номер банковской карты в формате XXXX XX** **** XXXX"""
    if len(card_number) <= 4:
        return card_number  # Возвращает номер без изменений, если он меньше или равен 4 символам
    elif len(card_number) < 6:
        return f"{card_number[:4]}**"  # Если длина 5, показывает 4 и маскирует остальные
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"  # Стандартный вариант


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер банковского счета в формате **XXXX"""
    if len(account_number) < 4:  # Возвращает номер без изменений, если он меньше 4 символов
        return account_number
    elif len(account_number) == 4:
        return f"**{account_number[-2:]}"
    return f"**{account_number[-4:]}"
