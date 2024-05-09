from datetime import datetime as dt
from datetime import timedelta

from src.types import Row


def parse(input: str) -> Row:
    inp = list(map(lambda s: s.strip(), input.split("-")))
    if len(inp) == 1:
        inp.append("")
    return inp


def get_today(days: float = 0) -> str:
    """Return date as today_date + days.
    days==0 -today, days==-1 -yesterday, days==1 -tomorrow."""
    return str(dt.today().date() + timedelta(days))
