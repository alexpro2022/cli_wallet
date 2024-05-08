from pprint import pprint

from src import constants as c
from src.commands import Command, Commands
from src.repository import create_repository
from src.utils import parse


def get_cmd_attr(cmd: str, attribute: str):
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


def input_cicle(file_path: str) -> int | str:
    try:
        cmd, flag = parse(input(c.INPUT_MSG))
        match cmd:
            case "/b":
                cmd = c.BALANCE_CMD
            case "/a":
                cmd = c.ADD_CMD
            case "/s":
                cmd = c.SEARCH_CMD
            case "/e":
                cmd = c.EDIT_CMD
            case "/q":
                cmd = c.EXIT_CMD
        if flag == c.DESCR_FLAG:
            return get_cmd_attr(cmd, "description")
        return get_cmd_attr(cmd, "handler")(file_path)
    except TypeError:
        return c.SOMETHING_WRONG_MSG


def app() -> int:
    file_path = create_repository()
    while True:
        res = input_cicle(file_path)
        if res == -1:
            return -1
        pprint(res)
