import pytest
from src.utils import read_json_file

def test_read_json_file_success():
    """Файл существует и содержит список — возвращает список"""
    data = read_json_file("data/operations.json")
    assert isinstance(data, list)
    assert len(data) > 0

def test_read_json_file_not_found():
    """Файл не найден — возвращает пустой список"""
    data = read_json_file("data/nonexistent.json")
    assert data == []

def test_read_json_file_empty(tmp_path):
    """Файл пустой — возвращает пустой список"""
    empty_file = tmp_path / "empty.json"
    empty_file.write_text("", encoding="utf-8")
    data = read_json_file(str(empty_file))
    assert data == []

def test_read_json_file_not_list(tmp_path):
    """Файл содержит не список (например, словарь) — возвращает пустой список"""
    not_list_file = tmp_path / "not_list.json"
    not_list_file.write_text('{"key": "value"}', encoding="utf-8")
    data = read_json_file(str(not_list_file))
    assert data == []

def test_read_json_file_invalid_json(tmp_path):
    """Файл с невалидным JSON — возвращает пустой список"""
    invalid_file = tmp_path / "invalid.json"
    invalid_file.write_text('{"key": "value"', encoding="utf-8")  # пропущена закрывающая скобка
    data = read_json_file(str(invalid_file))
    assert data == []