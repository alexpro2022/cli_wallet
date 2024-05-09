from decimal import Decimal

import pytest

from src.constants import CATEGORIES
from src.validators import get_valid_category, get_valid_decimal


@pytest.mark.parametrize("value", ("111", 111, 111.111))
def test_get_valid_decimal(value) -> None:
    assert get_valid_decimal(lambda _: value, "") == Decimal(value)


@pytest.mark.parametrize("value", (*CATEGORIES,))
def test_get_valid_category(value) -> None:
    assert get_valid_category(lambda _: value, "") in CATEGORIES
