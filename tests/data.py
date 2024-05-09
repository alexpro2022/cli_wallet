import pytest

from src.constants import BALANCE, CREDIT, DEBIT
from src.utils import get_today

DEBIT_SUM = 333
CREDIT_SUM = 222
BALANCE_SUM = DEBIT_SUM - CREDIT_SUM
EXPECTED_BALANCE_RESULT = (
    (f"{BALANCE}: {BALANCE_SUM}"),
    (f"{DEBIT}: {DEBIT_SUM}"),
    (f"{CREDIT}: {CREDIT_SUM}"),
)

TODAY = get_today()
FILE_PATH = "fake_file_path"
FILE_DATA = (
    (TODAY, DEBIT, DEBIT_SUM, "descr1"),
    (TODAY, CREDIT, CREDIT_SUM, "descr2"),
)

COMMAND_ATTRS = pytest.mark.parametrize("attr", ("description", "handler"))
SEARCH_PARAMS = pytest.mark.parametrize(
    "search_value, expected_result",
    (
        ("", []),
        (DEBIT, FILE_DATA[0]),
        (CREDIT, FILE_DATA[1]),
        (get_today(), FILE_DATA),
    ),
)
