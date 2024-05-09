import pytest

from src.constants import BALANCE, CREDIT, DEBIT
from src.utils import get_today

FILE_PATH = "fake_file_path"

TODAY = get_today()
YESTERDAY = get_today(-1)

DEBIT_SUM = 222
CREDIT_SUM = 111

FILE_DATA = (
    (TODAY, DEBIT, DEBIT_SUM, "descr1"),
    (YESTERDAY, DEBIT, DEBIT_SUM, "descr2"),
    (TODAY, CREDIT, CREDIT_SUM, "descr3"),
)

BALANCE_SUM = 2 * DEBIT_SUM - CREDIT_SUM

EXPECTED_BALANCE_RESULT = (
    (f"{BALANCE}: {BALANCE_SUM}"),
    (f"{DEBIT}: {2 * DEBIT_SUM}"),
    (f"{CREDIT}: {CREDIT_SUM}"),
)

# Pytest parameterization
COMMAND_ATTRS = pytest.mark.parametrize("attr", ("description", "handler"))
SEARCH_PARAMS = pytest.mark.parametrize(
    "search_value, expected_result",
    (
        ("", []),
        (DEBIT, FILE_DATA[0] + FILE_DATA[1]),
        (CREDIT, FILE_DATA[2]),
        (TODAY, FILE_DATA[0] + FILE_DATA[2]),
    ),
)
