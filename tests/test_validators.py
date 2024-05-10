from decimal import Decimal

import pytest

from src import constants as c
from src.validators import get_valid_category, get_valid_decimal


@pytest.mark.parametrize("value", ("111", 111, 111.111))
def test_get_valid_decimal(value) -> None:
    assert get_valid_decimal(lambda _: value, "") == Decimal(value)


@pytest.mark.parametrize("value", (*c.CATEGORIES,))
def test_get_valid_category(value) -> None:
    assert get_valid_category(lambda _: value, "") in c.CATEGORIES


@pytest.mark.parametrize(
    "invalid_input, valid_input, prompt_err, func",
    (
        ("asd", "доход", c.CATEGORY_INPUT_ERR_MSG, get_valid_category),
        ("asd", 111, c.DECIMAL_INPUT_ERR_MSG, get_valid_decimal),
    ),
)
def test_prompt_change_with_invalid_input(
    invalid_input, valid_input, prompt_err, func
) -> None:
    INITIAL_PROMPT = ""
    counter = 0

    def inp(prompt: str):
        nonlocal counter
        if not counter:  # first input with initial prompt
            counter += 1
            assert prompt == INITIAL_PROMPT
            return invalid_input
        else:  # second input - prompt has changed
            assert prompt == prompt_err
            return valid_input

    assert func(inp, INITIAL_PROMPT) == valid_input
