from typing import Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data() -> List[Dict[str, str]]:
    """Возвращает список словарей, каждый из которых содержит
    информацию о состоянии и дате транзакции"""
    return [
        {"state": "EXECUTED", "date": "2023-10-01"},
        {"state": "PENDING", "date": "2023-10-02"},
        {"state": "EXECUTED", "date": "2023-09-30"},
    ]


def test_filter_by_state(sample_data: List[Dict[str, str]]) -> None:
    """Функция для тестирования фильтрации списка словарей по номеру ключа"""
    result = filter_by_state(sample_data, 'EXECUTED')
    assert len(result) == 2


def test_sort_by_date(sample_data: List[Dict[str, str]]) -> None:
    """Функция для тестирования фильтрации списка словарей по дате"""
    sorted_data = sort_by_date(sample_data)
    assert sorted_data[0]['date'] == "2023-10-02"
