from src.masks import get_mask_card_number, get_mask_account


def main():
    """Основная функция для демонстрации работы модуля"""
    # Пример использования функции маскировки карты
    card_number = 7000792289606361
    masked_card = get_mask_card_number(card_number)
    print(f"Маска карты: {masked_card}")

    # Пример использования функции маскировки счета
    account_number = 73654108430135874305
    masked_account = get_mask_account(account_number)
    print(f"Маска счета: {masked_account}")


#if __name__ == "__main__":
    #main()

from src.widget import get_date
print(get_date("2024-03-11T02:26:18.671407"))
