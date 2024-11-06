import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [
    ("1234567812345678", "1234 56** **** 5678"),
    ("9876543210123456", "9876 54** **** 3456"),
    ("1234", "1234"),  # Ожидаем, что 4 символа не будут замаскированы
    ("12", "12"),      # Ожидаем, что 2 символа не будут замаскированы
    ("", ""),          # Ожидаем пустую строку
])
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    """Функция для тестирования номера карты"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    ("12345678901234567890", "**7890"),
    ("1234", "**34"),  # Ожидаем, что 4 символа будут замаскированы
    ("12", "12"),  # Ожидаем, что 2 символа не будут замаскированы
    ("", ""),          # Ожидаем пустую строку
])
def test_get_mask_account(account_number: str, expected: str) -> None:
    """Функция для тестирования номера аккаунта"""
    assert get_mask_account(account_number) == expected
