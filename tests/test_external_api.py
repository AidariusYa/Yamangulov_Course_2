from unittest.mock import patch

import pytest

from src.external_api import convert_currency


@patch('src.external_api.requests.get')
def test_convert_currency_usd_to_rub(mock_get):
    """Проверяет, что сумма конвертирована правильно"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'rates': {'RUB': 75}}

    transaction = {'amount': 100, 'currency': 'USD'}
    result = convert_currency(transaction)

    assert result == 7500.0


@patch('src.external_api.requests.get')
def test_convert_currency_eur_to_rub(mock_get):
    """Проверяет, что сумма конвертирована правильно"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'rates': {'RUB': 85}}

    transaction = {'amount': 100, 'currency': 'EUR'}
    result = convert_currency(transaction)

    assert result == 8500.0


@patch('src.external_api.requests.get')
def test_convert_currency_no_conversion(mock_get):
    """Проверяет, что сумма остается без изменений"""
    transaction = {'amount': 100, 'currency': 'RUB'}
    result = convert_currency(transaction)

    assert result == 100.0


@patch('src.external_api.requests.get')
def test_convert_currency_api_error(mock_get):
    """Ошибка сервера"""
    mock_get.return_value.status_code = 500

    transaction = {'amount': 100, 'currency': 'USD'}

    with pytest.raises(Exception, match="Error fetching exchange rates"):
        convert_currency(transaction)
