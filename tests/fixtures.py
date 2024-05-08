from typing import Callable

import pytest


@pytest.fixture
def mock_input(monkeypatch) -> Callable:
    def mock_input_with(input_value: str) -> None:
        monkeypatch.setattr("builtins.input", lambda _: input_value)

    return mock_input_with
