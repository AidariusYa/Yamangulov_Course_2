from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.transactions import read_transactions_from_csv, read_transactions_from_excel


def test_read_transactions_from_csv():
    """Заголовки и данные в формате .csv"""
    mock_data = "id,state,date,amount,currency_name,currency_code,from,to,description\n" \
                "650703,EXECUTED,2023-09-05T11:30:32Z,16210,SoL,PEN,Счет 58803664651298323391,Счет 39746506635466619397,Перевод организации"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        transactions = read_transactions_from_csv("transactions.csv")
        assert len(transactions) == 1
        assert transactions[0] == ({
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "SoL",
            "currency_code": "PEN",
            "from": "Счет 58803664651298323391",
            "to": "Счет 39746506635466619397",
            "description": "Перевод организации"
        })


def test_read_transactions_from_excel():
    """Заголовки и данные в формате .xlsx"""
    mock_data = pd.DataFrame({
        "id": [650703],
        "state": ["EXECUTED"],
        "date": ["2023-09-05T11:30:32Z"],
        "amount": [16210],
        "currency_name": ["SoL"],
        "currency_code": ["PEN"],
        "from": ["Счет 58803664651298323391"],
        "to": ["Счет 39746506635466619397"],
        "description": ["Перевод организации"]
    })
    with patch("pandas.read_excel", return_value=mock_data):
        transactions = read_transactions_from_excel("transactions_exel.xlsx")
        assert len(transactions) == 1
        assert transactions[0] == {
                                   "id": 650703,
                                   "state": "EXECUTED",
                                   "date": "2023-09-05T11:30:32Z",
                                   "amount": 16210,
                                   "currency_name": "SoL",
                                   "currency_code": "PEN",
                                   "from": "Счет 58803664651298323391",
                                   "to": "Счет 39746506635466619397",
                                   "description": "Перевод организации"}
