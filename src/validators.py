from decimal import Decimal, InvalidOperation
from typing import Callable

from src.constants import CATEGORIES, CATEGORY_INPUT_ERR_MSG, DECIMAL_INPUT_ERR_MSG


def get_valid_decimal(_input: Callable, prompt: str) -> Decimal:
    while True:
        try:
            return Decimal(_input(prompt))
        except InvalidOperation:
            prompt = DECIMAL_INPUT_ERR_MSG


def get_valid_category(_input: Callable, prompt: str) -> str:
    while True:
        category = _input(prompt)
        if category in CATEGORIES:
            return category
        prompt = CATEGORY_INPUT_ERR_MSG
