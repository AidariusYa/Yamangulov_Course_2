import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data():
    return [
        {"state": "EXECUTED", "date": "2023-10-01"},
        {"state": "PENDING", "date": "2023-10-02"},
        {"state": "EXECUTED", "date": "2023-09-30"},
    ]


def test_filter_by_state(sample_data):
    result = filter_by_state(sample_data, 'EXECUTED')
    assert len(result) == 2


def test_sort_by_date(sample_data):
    sorted_data = sort_by_date(sample_data)
    assert sorted_data[0]['date'] == "2023-10-02"
