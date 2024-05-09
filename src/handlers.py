from decimal import Decimal

import pandas as pd

from src import constants as c
from src.constants import BALANCE, CREDIT, DEBIT
from src.repository import read_csv, write_csv
from src.types import Rows
from src.utils import choose_row, get_new_data, get_today
from src.validators import get_valid_category, get_valid_decimal


def add_record(file_path: str) -> str:
    date = get_today()
    category = get_valid_category(input, "Введите категорию: ")
    value = get_valid_decimal(input, "Введите сумму: ")
    description = input("Введите описание: ")
    write_csv(file_path, [date, category, str(value), description])
    return c.RECORD_SAVED_MSG


def search_record(file_path: str, search_value: str | None = None) -> Rows:
    if search_value is None:
        search_value = input("Введите искомое значение: ")
        print("Найденные элементы: ")
    return [row for row in read_csv(file_path) if search_value in row]


def balance(file_path: str) -> tuple[str, str, str]:
    def _sum(rows: Rows):
        return sum(map(Decimal, [row[2] for row in rows]))

    def _f(name: str, value: Decimal) -> str:
        return f"{name}: {value}"

    debits, credits = [], []
    for row in read_csv(file_path):
        if DEBIT in row:
            debits.append(row)
        elif CREDIT in row:
            credits.append(row)
    debit, credit = _sum(debits), _sum(credits)
    balance = debit - credit
    return _f(BALANCE, balance), _f(DEBIT, debit), _f(CREDIT, credit)


def edit_record(file_path: str) -> None:
    """def choose_row(df, pagination: int = c.PAGINATION):
        start_pos = 0
        max_pos = len(df) - pagination
        prompt = c.EDIT_MSG
        while True:
            print(df[start_pos : start_pos + pagination])
            inp, _ = parse(input(prompt))
            prompt = c.EDIT_MSG
            match inp:
                case c.UP_CMD:
                    start_pos -= pagination
                    if start_pos < 0:
                        start_pos = 0
                        prompt = c.NO_SCROLL_UP_MSG
                case c.DOWN_CMD:
                    start_pos += pagination
                    if start_pos > max_pos:
                        start_pos = max_pos
                        prompt = c.NO_SCROLL_DOWN_MSG
                case _:
                    try:
                        return int(inp)
                    except ValueError:
                        prompt = c.SOMETHING_WRONG_MSG

    def get_new_data() -> None:
        # TODO: values validation (sum - to convert to Decimal)
        data = []
        while True:
            inp = input(c.INPUT_NEW_DATA_MSG)
            if inp == "/q":
                return data
            col_name, value = inp.split(" ")
            if col_name in c.CSV_HEADER:
                data.append((col_name, value))"""

    df = pd.read_csv(file_path)
    row = choose_row(df)
    new_data = get_new_data()
    if new_data:
        for col, value in new_data:
            df.loc[row, col] = value
        df.to_csv(file_path)
