from typing import Callable

import pytest


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
