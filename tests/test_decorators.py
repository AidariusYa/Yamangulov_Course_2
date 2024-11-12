import tempfile

import pytest

from src.decorators import log


def test_log_good(capsys):
    """Тестирует выполнение декорированной функции"""

    @log()
    def func(x, y):
        return x + y
    result = func(1, 2)
    assert result == 3


def test_log_good_file_log(capsys):
    """Тестирует запись в файл после успешного выполнения"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def func(x, y):
        return x + y
    func(1, 2)
    with open(log_file_path, 'r', encoding='utf-8') as file:
        logs = file.read()
    assert 'func ok\n' in logs


def test_log_exception(capsys):
    """Тестирует вывод после ошибки в консоль"""

    @log()
    def func(x, y):
        return x + y
    func(1, "2")
    captured = capsys.readouterr()
    assert "func error: TypeError. Inputs: (1, '2'), {}\n" in captured.out


def test_log_exception_file_log(capsys):
    """Тестирует запись в файл после ошибки"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def func(x, y):
        return x + y
    func(1, "2")
    with open(log_file_path, 'r', encoding='utf-8') as file:
        logs = file.read()
    assert "func error: TypeError. Inputs: (1, '2'), {}\n" in logs
