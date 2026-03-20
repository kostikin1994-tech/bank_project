"""
Модуль для работы с банковскими картами и счетами.
Содержит функции маскировки и форматирования.
"""

from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

    Аргументы:
        date_string (str): Дата в формате ISO (например, "2024-03-11T02:26:18.671407")

    Возвращает:
        str: Дата в формате "ДД.ММ.ГГГГ" (например, "11.03.2024")
    """
    try:
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Неверный формат даты")


def mask_account_card(card_info: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.

    Аргументы:
        card_info (str): Строка с типом и номером (например, "Visa Platinum 7000792289606361"
                         или "Счет 73654108430135874305")

    Возвращает:
        str: Строка с замаскированным номером

    Raises:
        ValueError: Если формат строки неверный или номер карты содержит не 16 цифр
    """
    print("3. mask_account_card вызвана")
    print(f"4. Получили: {card_info}")

    parts = card_info.rsplit(' ', 1)
    print(f"5. Разделили на: {parts}")

    if len(parts) != 2:
        raise ValueError("Неверный формат строки")

    card_type = parts[0]
    number = parts[1]
    print(f"6. Тип: {card_type}, номер: {number}")

    if card_type.lower() == 'счет':
        print("7. Это счет")
        masked_number = get_mask_account(int(number))
        return f"{card_type} {masked_number}"
    else:
        print("7. Это карта")
        if len(number) != 16:
            raise ValueError("Номер карты должен содержать 16 цифр")
        masked_number = get_mask_card_number(int(number))
        return f"{card_type} {masked_number}"


if __name__ == '__main__':
    print("Тестирование функций:")
    print(get_date("2024-03-11T02:26:18.671407"))
    print(mask_account_card("Visa Platinum 7000792289606361"))
