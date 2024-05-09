import pytest

from src import constants as c
from src.handlers import add_record, search_record
from src.types import Row
from src.utils import get_today
from src.validators import Decimal, get_valid_category, get_valid_decimal
from tests.data import FILE_DATA, FILE_PATH

search_params = pytest.mark.parametrize(
    "search_value, expected_result",
    (
        ("", []),
        (c.DEBIT, FILE_DATA[0]),
        (c.CREDIT, FILE_DATA[1]),
        (get_today(), FILE_DATA),
    ),
)


@search_params
def test_search_record_without_manual_input(
    search_setup, search_value, expected_result
) -> None:
    search_record(FILE_PATH, search_value) == expected_result


@search_params
def test_search_record_with_manual_input(
    mock_input, search_setup, search_value, expected_result
) -> None:
    mock_input(search_value)
    search_record(FILE_PATH) == expected_result


def test_add_record(monkeypatch, mock_input) -> None:
    def mock_get_valid_category(*args, **kwargs) -> str:
        mock_input(c.DEBIT)
        return get_valid_category(input, "")

    def mock_get_valid_decimal(*args, **kwargs) -> Decimal:
        mock_input("111.111")
        res = get_valid_decimal(input, "")
        mock_input("description")
        return res

    def mock_write_csv(file_path: str, row: Row) -> None:
        assert file_path == FILE_PATH
        assert row[0] == get_today()
        assert row[1] == c.DEBIT
        assert row[2] == "111.111"
        assert row[3] == "description"

    monkeypatch.setattr("src.handlers.get_valid_category", mock_get_valid_category)
    monkeypatch.setattr("src.handlers.get_valid_decimal", mock_get_valid_decimal)
    monkeypatch.setattr("src.handlers.write_csv", mock_write_csv)
    assert add_record(FILE_PATH) == c.RECORD_SAVED_MSG
