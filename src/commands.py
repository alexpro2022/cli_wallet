from dataclasses import dataclass
from typing import Callable

from . import constants as c
from . import handlers as h


@dataclass
class Command:
    name: str
    description: str
    handler: Callable


class Commands:
    balance = Command(c.BALANCE_CMD, c.BALANCE_CMD_DESCR, h.balance)
    add_record = Command(c.ADD_CMD, c.ADD_CMD_DESCR, h.add_record)
    edit_record = Command(c.EDIT_CMD, c.EDIT_CMD_DESCR, h.edit_record)
    search_record = Command(c.SERACH_CMD, c.SERACH_CMD_DESCR, h.search_record)
    exit = Command(c.EXIT_CMD, c.EXIT_CMD_DESCR, lambda _: -1)
