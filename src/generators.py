def filter_by_currency(transactions, currency):
    """
        Принимает писок словарей и возвращает по
        очереди транзакции по заданной валюте.
        """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """
        Принимает список словарей и возвращает
        тип операции.
        """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    """
        Генерирует номер карты в формате
        'XXXX XXXX XXXX XXXX' по очереди.
        """
    for number in range(start, end + 1):
        num_str = str(number).zfill(16)
        parts = [num_str[i:i+4] for i in range(0, 16, 4)]
        formatted = " ".join(parts)
        yield formatted



