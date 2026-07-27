import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/app.log', mode='w', encoding="utf-8")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маску номера банковской карты.

    Маска представляет собой строку вида:
    XXXX XX** **** XXXX
    Где XXXX - первые 4 цифры, XXXX - последние 4 цифры
    """
    logger.info(f'Получение номера карты: {card_number}')
    card_str = str(card_number)

    if len(card_str) != 16:
        logger.error('Некорректный номер карты')
        raise ValueError("Номер карты должен содержать 16 цифр")

    masked = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    logger.info('Функция успешно выполнена')
    return masked

def get_mask_account(account_number: int) -> str:
    """
    Возвращает маску номера банковского счета.

    Маска представляет собой строку вида:
    **XXXX
    Где XXXX - последние 4 цифры счета
    """

    logger.info(f'Получение номера счета: {account_number}')
    account_str = str(account_number)

    if len(account_str) < 4:
        logger.error('Некорректный номер счета')
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    masked = f"**{account_str[-4:]}"
    logger.info('Функция успешно выполнена')
    return masked

if __name__ == '__main__':
    card = get_mask_account(12)
    print(card)
