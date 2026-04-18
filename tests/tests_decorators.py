import pytest
import logging
from src.decorators import log


def test_log_to_file(tmp_path):
    """Тест: декоратор записывает логи в файл."""
    log_file = tmp_path / "test.log"

    # Очищаем логгер перед тестом
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    result = multiply(4, 5)
    assert result == 20

    # Проверяем, что файл создался
    assert log_file.exists()

    # Проверяем содержимое файла
    content = log_file.read_text(encoding="utf-8")
    assert "multiply ok. Result: 20" in content


def test_log_multiple_calls(tmp_path):
    """Тест: при нескольких вызовах логи дописываются в файл."""
    log_file = tmp_path / "append.log"

    # Очищаем логгер перед тестом
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    @log(filename=str(log_file))
    def add(a, b):
        return a + b

    add(1, 1)  # результат 2
    add(2, 2)  # результат 4

    # Проверяем, что файл создался
    assert log_file.exists()

    content = log_file.read_text(encoding="utf-8")
    # Проверяем, что обе записи присутствуют
    assert "add ok. Result: 2" in content
    assert "add ok. Result: 4" in content
    # И что в файле две строки (два лога)
    assert content.count("add ok.") == 2


def test_log_no_file():
    """Тест: декоратор без параметра не вызывает ошибок."""
    @log()
    def dummy():
        return 42

    result = dummy()
    assert result == 42


def test_log_exception():
    """Тест: декоратор пробрасывает исключение."""
    @log()
    def div(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)