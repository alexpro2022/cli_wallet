from datetime import datetime as dt

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


def test_get_today() -> None:
    assert isinstance(get_today(), str)
    assert get_today() == str(dt.today().date())
