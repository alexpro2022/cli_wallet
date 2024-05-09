from pandas import DataFrame

from src import constants as c
from src.handlers import add_record, balance, edit_record, search_record
from tests.data import EXPECTED_BALANCE_RESULT, FILE_DATA, FILE_PATH, SEARCH_PARAMS


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


def test_edit_record(monkeypatch) -> None:
    ROW = 1
    NEW_DATA = [
        ("Категория", "расход"),
        ("Сумма", "123"),
        ("Описание", "Описание расходов"),
    ]

    class DF(DataFrame):
        def to_csv(self, *args, **kwargs):
            assert "расход   123  Описание расходов" in str(self)

    monkeypatch.setattr("pandas.read_csv", lambda _: DF(FILE_DATA))
    monkeypatch.setattr("src.handlers.choose_row", lambda _: ROW)
    monkeypatch.setattr("src.handlers.get_new_data", lambda: NEW_DATA)
    monkeypatch.setattr("pandas.DataFrame", lambda: DF)
    edit_record(FILE_PATH)
