from unittest.mock import patch
from src.file_reader import (pandas_read_csv, pandas_read_excel)
import pandas as pd

def test_pandas_read_csv():
    mock_data = pd.DataFrame([{'id' : 1, 'Amount' : 100}])
    with patch('src.file_reader.pd.read_csv', return_value=mock_data):
        result = pandas_read_csv('any_path.csv')

        assert len(result) == 1
        assert result[0]['id'] == 1


def test_pandas_read_excel():
    mock_data = pd.DataFrame([{'id': 1, 'amount': 100}])
    with patch('src.file_reader.pd.read_excel', return_value=mock_data):
        result = pandas_read_excel('any_path.xlsx')

        assert len(result) == 1
        assert result[0]['id'] == 1

def test_pandas_read_csv_empty():
    mock_data = pd.DataFrame()
    with patch('src.file_reader.pd.read_csv', return_value=mock_data):
        result = pandas_read_csv('empty.csv')
        assert result == []

def test_pandas_read_csv_not_found():
    with patch('src.file_reader.pd.read_csv', side_effect=FileNotFoundError):
        result = pandas_read_csv('missing.csv')
        assert result == []

def test_pandas_read_csv_generic_error():
    with patch('src.file_reader.pd.read_csv', side_effect=Exception("Something wrong")):
        result = pandas_read_csv('any.csv')
        assert result == []

def test_pandas_read_excel_empty():
    mock_data = pd.DataFrame()
    with patch('src.file_reader.pd.read_excel', return_value=mock_data):
        result = pandas_read_excel('empty.xlsx')
        assert result == []

def test_pandas_read_excel_not_found():
    with patch('src.file_reader.pd.read_excel', side_effect=FileNotFoundError):
        result = pandas_read_excel('missing.xlsx')
        assert result == []

def test_pandas_read_excel_generic_error():
    with patch('src.file_reader.pd.read_excel', side_effect=Exception("Something wrong")):
        result = pandas_read_excel('any.xlsx')
        assert result == []


