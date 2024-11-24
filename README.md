# Проект Yamangulov_Course_2
## Цель проекта
Целью проекта является создания новой ветки репозитория и 
создание словарей, отсортированных по ключу и по дате.

## Установка
Клонируйте репозиторий:
```
git clone https://github.com/AidariusYa/advanced_git.git
``` 

Установите зависимости:
```
pip install -r requirements.txt
```

Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

Запустите локальный сервер:
```
python manage.py runserver
```

## Использование

# Модуль 
Transactions

## Описание

Модуль `transactions` содержит функции для чтения содержимого файлов формата csv
и xlsx. Они позволяют видеть всю необходимую информацию о финансовых операциях.
### Примеры использования функций:

read_transactions_from_csv(file_path) Функция Считывает финансовые операции 
из CSV файла и возвращает список словарей с транзакциями с занесением 
результатов в лог.

```
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
```

read_transactions_from_excel(file_path) Функция считывает финансовые операции из
Excel файла и возвращает список словарей с транзакциямис занесением 
результатов в лог.
### Примеры использования функций:

```
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
```

# Модуль 
Generators

## Описание

Модуль `generators` содержит функции-генераторы для обработки данных 
транзакций. Он позволяет фильтровать транзакции по валюте, получать 
описания транзакций и генерировать номера банковских карт.
### Примеры использования функций:

filter_by_currency(transactions, currency)
Функция фильтрует транзакции по заданной валюте и возвращает итератор, 
который поочередно выдает транзакции, где валюта операции соответствует 
заданной.
```
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```

transaction_descriptions(transactions)
Генератор, который принимает список словарей с транзакциями и 
возвращает описание каждой операции по очереди.

```
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```

card_number_generator(start, stop)
Генератор, который выдает номера банковских карт в формате 
XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может 
сгенерировать номера карт в заданном диапазоне 
от 0000 0000 0000 0001 до 9999 9999 9999 9999.

```
for card_number in card_number_generator(1, 5):
    print(card_number)
```

#### Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

#### Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

#### Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
## Тестирование

Для выполнения тестирования всех функций выполните команду:
```
pytest --cov=src --cov-report=html
```

## Документация:

Дополнительную информацию о структуре проекта и API можно найти в документации.

## Лицензия:

Проект распространяется под лицензией SuperSkyPro.
