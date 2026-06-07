import os
import requests

def currency_converter(transaction):
    amount = float(transaction['operationAmount']['amount'])
    currency_code = transaction['operationAmount']['currency']['code']

    if currency_code == 'RUB':
        return amount

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency_code}&symbols=RUB"
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()
        rate = data['rates']['RUB']
        return amount * rate
    except Exception:
        return None

