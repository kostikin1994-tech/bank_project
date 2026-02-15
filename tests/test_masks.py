import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    """Тест маскировки номера карты"""
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"
    assert get_mask_card_number(1234567812345678) == "1234 56** **** 5678"


def test_get_mask_card_number_invalid():
    """Тест на некорректный номер карты"""
    with pytest.raises(ValueError):
        get_mask_card_number(12345)
    with pytest.raises(ValueError):
        get_mask_card_number(123456781234567890)


def test_get_mask_account():
    """Тест маскировки номера счета"""
    assert get_mask_account(73654108430135874305) == "**4305"
    assert get_mask_account(12345678) == "**5678"


def test_get_mask_account_invalid():
    """Тест на некорректный номер счета"""
    with pytest.raises(ValueError):
        get_mask_account(123)
