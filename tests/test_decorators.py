import pytest
from src.decorators import log


def test_log_to_file(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    result = multiply(4, 5)
    assert result == 20
    assert log_file.exists()

    content = log_file.read_text(encoding="utf-8")
    assert "multiply ok" in content


def test_log_multiple_calls(tmp_path):
    log_file = tmp_path / "append.log"

    @log(filename=str(log_file))
    def add(a, b):
        return a + b

    add(1, 1)
    add(2, 2)

    content = log_file.read_text(encoding="utf-8")
    assert content.count("add ok") == 2


def test_log_exception(capsys):
    @log()
    def div(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    captured = capsys.readouterr()
    assert "ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0)" in captured.out
