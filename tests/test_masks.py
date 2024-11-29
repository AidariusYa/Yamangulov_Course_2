import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_info, expected", [
    ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
    ("Master Card 9876543210123456", "Master Card 9876 54** **** 3456"),
    ("МИР 1234", "МИР 1234"),  # Ожидаем, что 4 символа не будут замаскированы
    ("Maestro 12", "Maestro 12"),           # Ожидаем, что 2 символа не будут замаскированы
    ("", "Нет данных о карте"),     # Ожидаем сообщение о том, что нет данных
])
def test_get_mask_card_number(card_info: str, expected: str) -> None:
    """Функция для тестирования номера карты"""
    assert get_mask_card_number(card_info) == expected


@pytest.mark.parametrize("account_number, expected", [
    ("Счет 12345678901234567890", "Счет **7890"),
    ("1234", "Счет **34"),  # Ожидаем, что 4 символа будут замаскированы
    ("12", "Счет 12"),      # Ожидаем, что 2 символа не будут замаскированы
    ("", "Нет данных о счете"),  # Ожидаем сообщение о том, что нет данных
])
def test_get_mask_account(account_number: str, expected: str) -> None:
    """Функция для тестирования номера аккаунта"""
    assert get_mask_account(account_number) == expected
