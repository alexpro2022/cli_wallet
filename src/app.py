from . import constants as c
from .commands import Command, Commands
from .utils import create_repository, parse


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
    cmd, flag = parse(input(c.INPUT_MSG))
    if flag == c.DESCR_FLAG:
        return get_cmd_attr(cmd, "description")
    else:
        return get_cmd_attr(cmd, "handler")(file_path)


def app() -> int:
    file_path = create_repository()
    while True:
        res = input_cicle(file_path)
        if res == -1:
            return -1
        print(res)
