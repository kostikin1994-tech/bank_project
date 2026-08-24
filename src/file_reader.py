import pandas as pd
import json


def pandas_read_csv(file_name):
    '''Функция для чтения файлов формата csv, возвращает список словарей.'''
    try:
        df = pd.read_csv(file_name)
        return df.to_dict('records')
    except FileNotFoundError:
        return []  # или raise
    except Exception:
        return []

def pandas_read_excel(file_name):
    '''Функция для чтения файлов формата Excel, возвращает список словарей.'''
    try:
        df = pd.read_excel(file_name)
        return df.to_dict('records')
    except FileNotFoundError:
        return []
    except Exception:
        return []

def pandas_read_json(file_name):
    '''Функция для чтения файлов формата JSON, возвращает список словарей.'''
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except Exception:
        return []

if __name__ == '__main__':
    csv_data = pandas_read_csv('data/transactions.csv')
    print(csv_data[:3])
    excel_data = pandas_read_excel('data/transactions_excel.xlsx')
    print(excel_data[:3])


