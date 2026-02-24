def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маску номера банковской карты.

    Маска представляет собой строку вида:
    XXXX XX** **** XXXX
    Где XXXX - первые 4 цифры, XXXX - последние 4 цифрыrm
    """
    card_str = str(card_number)

    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    # Формат: 7000 79** **** 6361
    masked = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    return masked


def get_mask_account(account_number: int) -> str:
    """
    Возвращает маску номера банковского счета.

    Маска представляет собой строку вида:
    **XXXX
    Где XXXX - последние 4 цифры счета
    """
    account_str = str(account_number)

    if len(account_str) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    masked = f"**{account_str[-4:]}"
    return masked
