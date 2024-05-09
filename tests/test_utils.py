from datetime import datetime as dt
from datetime import timedelta

import pytest

from src.utils import get_today, parse


@pytest.mark.parametrize(
    "input, expected",
    (
        ("cmd-flag", ["cmd", "flag"]),
        (" cmd - flag ", ["cmd", "flag"]),
        ("cmd", ["cmd", ""]),
    ),
)
def test_parse(input, expected) -> None:
    assert parse(input) == expected


@pytest.mark.parametrize("days", (-1, 0, 1))
def test_get_today(days) -> None:
    assert isinstance(get_today(), str)
    assert get_today(days) == str(dt.today().date() + timedelta(days))
