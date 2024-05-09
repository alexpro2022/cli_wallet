from src import constants as c
from src.handlers import add_record, balance, search_record
from tests.data import EXPECTED_BALANCE_RESULT, FILE_PATH, SEARCH_PARAMS


@SEARCH_PARAMS
def test_search_record_without_manual_input(
    search_setup, search_value, expected_result
) -> None:
    search_record(FILE_PATH, search_value) == expected_result


@SEARCH_PARAMS
def test_search_record_with_manual_input(
    mock_input, search_setup, search_value, expected_result
) -> None:
    mock_input(search_value)
    search_record(FILE_PATH) == expected_result


def test_balance(search_setup) -> None:
    assert balance(FILE_PATH) == EXPECTED_BALANCE_RESULT


def test_add_record(add_setup) -> None:
    assert add_record(FILE_PATH) == c.RECORD_SAVED_MSG
