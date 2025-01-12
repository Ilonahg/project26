def filter_by_currency(transactions, currency):
    """Фильтрует транзакции по валюте."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Генерирует описание транзакций по очереди."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, stop):
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX."""
    for i in range(start, stop + 1):
        card_number = f"{i:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
