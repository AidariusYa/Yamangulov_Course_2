import pytest
from src.widjet import mask_account_card, get_date


@pytest.mark.parametrize("card_info, expected", [
    ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
    ("Count 12345678901234567890", "Count **7890"),
])
def test_mask_account_card(card_info, expected):
    assert mask_account_card(card_info) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2023-10-01", "01.10.2023"),
    ("2022-01-15", "15.01.2022"),
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
