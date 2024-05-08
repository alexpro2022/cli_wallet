from datetime import datetime as dt

from src.types import Row


def parse(input: str) -> Row:
    inp = list(map(lambda s: s.strip(), input.split("-")))
    if len(inp) == 1:
        inp.append("")
    return inp


def get_today() -> str:
    return str(dt.today().date())
