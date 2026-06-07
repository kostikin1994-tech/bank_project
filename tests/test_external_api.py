import pytest
from src.external_api import currency_converter

def test_currency_converter_rub():
    """Если валюта RUB, возвращается сумма без конвертации"""
    transaction = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {"code": "RUB"}
        }
    }
    assert currency_converter(transaction) == 100.50

def test_currency_converter_usd(mocker):
    """Конвертация USD в рубли через API"""
    # Подменяем requests.get, чтобы не ходить в реальное API
    mock_get = mocker.patch("src.external_api.requests.get")
    mock_get.return_value.json.return_value = {"rates": {"RUB": 90.0}}

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }
    assert currency_converter(transaction) == 9000.0

def test_currency_converter_eur(mocker):
    """Конвертация EUR в рубли через API"""
    mock_get = mocker.patch("src.external_api.requests.get")
    mock_get.return_value.json.return_value = {"rates": {"RUB": 100.0}}

    transaction = {
        "operationAmount": {
            "amount": "50",
            "currency": {"code": "EUR"}
        }
    }
    assert currency_converter(transaction) == 5000.0

def test_currency_converter_api_error(mocker):
    """Если API вернул ошибку, функция возвращает None (или можно raise)"""
    mock_get = mocker.patch("src.external_api.requests.get")
    mock_get.side_effect = Exception("API not available")

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }
    assert currency_converter(transaction) is None
