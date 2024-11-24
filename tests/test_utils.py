from unittest.mock import mock_open, patch

import pytest

from src.utils import read_json_file


def test_read_json_file_valid():
    """Проверяет, что функция правильно читает валидный JSON - файл"""
    mock_data = '[{"amount": 100, "currency": "RUB"}]'
    with (patch("builtins.open", mock_open(read_data=mock_data)),
         patch("os.path.exists", return_value=True)):  # Чтобы всегда показывал, что файл существует
        result = read_json_file("data/operations.json")
        assert len(result) == 1
        assert result[0]["amount"] == 100
        assert result[0]["currency"] == "RUB"


def test_read_json_file_empty_file():
    """ Проверяет, что функция возвращает пустой список для пустого файла"""
    with patch("builtins.open", mock_open(read_data='')):
        result = read_json_file('data/empty.json')
        assert result == []


def test_read_json_file_invalid_json():
    """Проверяет, что функция возвращает пустой список для файла с некорректным JSON"""
    with patch("builtins.open", mock_open(read_data='invalid json')):
        result = read_json_file('data/invalid.json')
        assert result == []


def test_read_json_file_file_not_found():
    """Проверяет, что функция возвращает пустой список, если файл не найден"""
    result = read_json_file('data/non_existent.json')
    assert result == []
