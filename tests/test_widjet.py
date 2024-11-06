import pytest

from src.widjet import get_date, mask_account_card


@pytest.mark.parametrize("card_info, expected", [
    ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
    ("Count 12345678901234567890", "Count **7890"),
])
def test_mask_account_card(card_info: str, expected: str) -> None:
    """Функция для тестирования тестирования маскировки номера карты и аккаунта"""
    assert mask_account_card(card_info) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2023-10-01", "01.10.2023"),
    ("2022-01-15", "15.01.2022"),
])
def test_get_date(date_str: str, expected: str) -> None:
    """Функция для тестирования преобразования строки с датой"""
    assert get_date(date_str) == expected
