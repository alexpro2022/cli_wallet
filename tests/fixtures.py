from typing import Callable

import pytest

from src import constants as c
from src.constants import ENCODING
from src.types import Row
from src.utils import get_today
from src.validators import Decimal, get_valid_category, get_valid_decimal
from tests.data import FILE_DATA, FILE_PATH


@pytest.fixture
def mock_input(monkeypatch) -> Callable:
    def mock_input_with(input_value: str = "") -> None:
        monkeypatch.setattr("builtins.input", lambda _: input_value)

    return mock_input_with


@pytest.fixture
def mock_os_dir(monkeypatch) -> Callable:
    def mock_os_dir_with(mock_func: Callable = lambda _: ...) -> None:
        monkeypatch.setattr("os.mkdir", mock_func)
        monkeypatch.setattr("os.path.exists", lambda _: True)

    return mock_os_dir_with


@pytest.fixture
def search_setup(monkeypatch):
    def mock_read_csv(file_path):
        assert file_path == FILE_PATH
        yield from FILE_DATA

    monkeypatch.setattr("src.handlers.handlers.read_csv", mock_read_csv)


@pytest.fixture
def mock_open_file(monkeypatch):
    def _mock_open_file(*args, **kwargs):
        class FakeFIle:
            def __enter__(*args, **kwargs): ...
            def __exit__(*args, **kwargs): ...

        assert args[0] == FILE_PATH
        assert args[1] in ("a", "r")
        assert kwargs == ENCODING
        return FakeFIle()

    monkeypatch.setattr("builtins.open", _mock_open_file)


@pytest.fixture
def add_setup(monkeypatch, mock_input):
    def mock_get_valid_category(*args, **kwargs) -> str:
        mock_input(c.DEBIT)
        return get_valid_category(input, "")

    def mock_get_valid_decimal(*args, **kwargs) -> Decimal:
        mock_input("111.111")
        res = get_valid_decimal(input, "")
        mock_input("description")
        return res

    def mock_write_csv(file_path: str, row: Row) -> None:
        assert file_path == FILE_PATH
        assert row[0] == get_today()
        assert row[1] == c.DEBIT
        assert row[2] == "111.111"
        assert row[3] == "description"

    monkeypatch.setattr(
        "src.handlers.handlers.get_valid_category", mock_get_valid_category
    )
    monkeypatch.setattr(
        "src.handlers.handlers.get_valid_decimal", mock_get_valid_decimal
    )
    monkeypatch.setattr("src.handlers.handlers.write_csv", mock_write_csv)
