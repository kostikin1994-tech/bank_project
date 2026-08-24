def filter_by_state(transactions: list, state: str = "EXECUTED") -> list:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Аргументы:
        transactions (list): Список словарей с ключом 'state'
        state (str): Значение для фильтрации (по умолчанию 'EXECUTED')

    Возвращает:
        list: Новый список, содержащий только словари с указанным state
    """
    return [item for item in transactions if item.get("state") == state]


def sort_by_date(transactions: list, reverse: bool = True) -> list:
    """
    Сортирует список словарей по дате (ключ 'date').

    Аргументы:
        transactions (list): Список словарей с ключом 'date'
        reverse (bool): Если True — по убыванию (сначала новые), если False — по возрастанию

    Возвращает:
        list: Новый отсортированный список
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)