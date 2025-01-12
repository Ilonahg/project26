# Project 26

Это проект, в котором реализованы генераторы для работы с транзакциями и номерами карт.

## Функции

### 1. filter_by_currency
Функция для фильтрации транзакций по валюте.

#### Пример использования:

```python
from generators import filter_by_currency

transactions = [
    {
        "operationAmount": {
            "currency": {"code": "USD"}
        }
    },
    {
        "operationAmount": {
            "currency": {"code": "RUB"}
        }
    }
]

filtered = filter_by_currency(transactions, "USD")
print(list(filtered))  # Выведет только транзакции с валютой USD
