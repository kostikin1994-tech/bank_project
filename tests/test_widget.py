import pytest
from src.widget import mask_account_card, get_date


def test_mask_account_card(sample_card_strings):
    """Тестирует маскировку карт и счетов."""
    for input_str, expected in sample_card_strings:
        assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("input_str", [
    "",
    "Visa",
    "1234567890123456",
])
def test_mask_account_card_invalid(input_str):
    """Тестирует некорректные входные данные."""
    with pytest.raises(ValueError):
        mask_account_card(input_str)


@pytest.mark.parametrize("input_date", [
    "",
    "2024-13-01T00:00:00",
    "not-a-date",
])
def test_get_date_invalid(input_date):
    """Тестирует некорректные форматы даты."""
    with pytest.raises(ValueError):
        get_date(input_date)