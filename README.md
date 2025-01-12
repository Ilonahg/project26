# Transaction Generators

Модуль для работы с транзакциями, включая генераторы для фильтрации транзакций по валюте, получения описаний операций и генерации номеров карт.

## Пример использования

### Фильтрация транзакций по валюте:

```python
from generators.generators import filter_by_currency

transactions = [
    # Пример транзакций...
]

usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)
