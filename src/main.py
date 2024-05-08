from dataclasses import dataclass
from typing import Callable

if __package__:
    from . import constants as c
    from . import handlers as h
    from .utils import parse
else:
    import constants as c  # type: ignore [no-redef]
    import handlers as h  # type: ignore [no-redef]
    from utils import parse  # type: ignore [no-redef]


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
    exit = Command(c.EXIT_CMD, c.EXIT_CMD_DESCR, lambda: -1)


def get_cmd_attr(cmd: str, attribute: str):  # -> str | Callable:
    actual_commands: list[Command] = list(
        map(
            lambda command: getattr(Commands, command),
            filter(lambda attr: not attr.startswith("__"), dir(Commands)),
        )
    )
    for command in actual_commands:
        if command.name == cmd:
            return getattr(command, attribute)
    return c.HELP_MSG


def input_cicle() -> int | str:
    cmd, flag = parse(input(c.INPUT_MSG))
    if flag == c.DESCR_FLAG:
        return get_cmd_attr(cmd, "description")
    else:
        return get_cmd_attr(cmd, "handler")()


def main() -> int:
    while True:
        res = input_cicle()
        if res == -1:
            return -1
        print(res)


if __name__ == "__main__":
    main()
