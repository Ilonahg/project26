import pytest
from generators.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Фикстура для создания данных транзакций
@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "RUB", "code": "RUB"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
    ]

# Параметризированные тесты
@pytest.mark.parametrize(
    "currency, expected_count",
    [("USD", 2), ("RUB", 1), ("EUR", 0)]
)
def test_filter_by_currency(sample_transactions, currency, expected_count):
    filtered_transactions = filter_by_currency(sample_transactions, currency)
    count = sum(1 for _ in filtered_transactions)
    assert count == expected_count

def test_transaction_descriptions(sample_transactions):
    descriptions = transaction_descriptions(sample_transactions)
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет"
    ]
    for expected_description, description in zip(expected_descriptions, descriptions):
        assert description == expected_description

@pytest.mark.parametrize(
    "start, stop, expected_count",
    [(1, 5, 5), (999, 1003, 5), (1000, 1000, 1)]
)
def test_card_number_generator(start, stop, expected_count):
    generated_cards = list(card_number_generator(start, stop))
    assert len(generated_cards) == expected_count
    for card in generated_cards:
        assert len(card) == 19  # Проверка формата XXXX XXXX XXXX XXXX
        assert card.replace(" ", "").isdigit()  # Проверка, что все символы - цифры
