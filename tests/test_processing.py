import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(sample_transactions):
    """Тестирует фильтрацию по умолчанию (EXECUTED)."""
    result = filter_by_state(sample_transactions)
    expected = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]
    assert result == expected


def test_filter_by_state_canceled(sample_transactions):
    """Тестирует фильтрацию с явным аргументом CANCELED."""
    result = filter_by_state(sample_transactions, state="CANCELED")
    expected = [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]
    assert result == expected


def test_filter_by_state_empty(sample_transactions):
    """Тестирует фильтрацию со статусом, которого нет в списке."""
    result = filter_by_state(sample_transactions, state="PENDING")
    assert result == []


def test_sort_by_date_default(sample_transactions):
    """Тестирует сортировку по умолчанию (убывание, reverse=True)."""
    result = sort_by_date(sample_transactions)
    expected = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]
    assert result == expected


def test_sort_by_date_ascending(sample_transactions):
    """Тестирует сортировку по возрастанию (reverse=False)."""
    result = sort_by_date(sample_transactions, reverse=False)
    expected = [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    ]
    assert result == expected
