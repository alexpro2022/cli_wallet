from typing import Callable

import pytest

from src.constants import ENCODING
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

    monkeypatch.setattr("src.handlers.read_csv", mock_read_csv)


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
