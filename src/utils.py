from datetime import datetime as dt
from datetime import timedelta

from pandas import DataFrame

from src import constants as c
from src.types import EditData, Row


def parse(input: str) -> Row:
    inp = list(map(lambda s: s.strip(), input.split("-")))
    if len(inp) == 1:
        inp.append("")
    return inp


def get_today(days: float = 0) -> str:
    """Return date as today_date + days.
    days==0 -today, days==-1 -yesterday, days==1 -tomorrow."""
    return str(dt.today().date() + timedelta(days))


def choose_row(df: DataFrame, pagination: int = c.PAGINATION):
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


def get_new_data() -> EditData:
    # TODO: values validation (sum - to convert to Decimal)
    data: EditData = []
    while True:
        inp = input(c.INPUT_NEW_DATA_MSG)
        if inp == "/q":
            return data
        col_name, value = inp.split(" ")
        if col_name in c.CSV_HEADER:
            data.append((col_name, value))
