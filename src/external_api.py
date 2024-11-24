import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_currency(transaction):
    """Принимает словарь с данными о транзакции и возвращает сумму в рублях"""
    amount = transaction['amount']
    currency = transaction['currency']

    if currency not in ['USD', 'EUR']:
        return float(amount)

    api_key = os.getenv('API_KEY')
    response = requests.get(f'https://api.apilayer.com/exchangerates_data/latest?base={currency}&apikey={api_key}')
    if response.status_code == 200:
        rates = response.json().get('rates', {})
        rub_rate = rates.get('RUB', 1)
        return float(amount) * rub_rate
    else:
        raise Exception("Error fetching exchange rates")


if __name__ == "__main__":
    transaction = {'amount': 100, 'currency': 'USD'}
    rub_amount = convert_currency(transaction)
    print(f"Сумма в рублях: {rub_amount}")
