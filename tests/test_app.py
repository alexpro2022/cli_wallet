from src import constants as c
from src.app import app, get_cmd_attr, input_cicle
from src.commands import Commands
from tests.data import COMMAND_ATTRS, FILE_PATH, pytest


@COMMAND_ATTRS
def test_get_attr_invalid_command(attr) -> None:
    invalid_command = "/"
    assert get_cmd_attr(invalid_command, attr) == c.HELP_MSG


@COMMAND_ATTRS
@pytest.mark.parametrize(
    "cmd_name, expected_command",
    (
        (c.BALANCE_CMD, Commands.balance),
        (c.ADD_CMD, Commands.add_record),
        (c.EDIT_CMD, Commands.edit_record),
        (c.SEARCH_CMD, Commands.search_record),
        (c.EXIT_CMD, Commands.exit),
    ),
)
def test_get_attr(cmd_name, expected_command, attr) -> None:
    assert get_cmd_attr(cmd_name, attr) == getattr(expected_command, attr)


@pytest.mark.parametrize(
    "cmd_name, expected_descr",
    (
        (c.BALANCE_CMD, c.BALANCE_CMD_DESCR),
        (c.ADD_CMD, c.ADD_CMD_DESCR),
        (c.EDIT_CMD, c.EDIT_CMD_DESCR),
        (c.SEARCH_CMD, c.SEARCH_CMD_DESCR),
        (c.EXIT_CMD, c.EXIT_CMD_DESCR),
    ),
)
def test_input_cicle_return_description(mock_input, cmd_name, expected_descr) -> None:
    mock_input(f"{cmd_name}-d")
    assert input_cicle(FILE_PATH) == expected_descr


@pytest.mark.parametrize(
    "cmd_name, expected_handler_result",
    (
        # (c.BALANCE_CMD, EXPECTED_BALANCE_RESULT),
        # ("/b", EXPECTED_BALANCE_RESULT),
        (c.ADD_CMD, c.RECORD_SAVED_MSG),
        ("/a", c.RECORD_SAVED_MSG),
        # (c.EDIT_CMD, h.edit_record),
        # ("/e", h.edit_record),
        (c.SEARCH_CMD, []),
        ("/s", []),
        (c.EXIT_CMD, -1),
        ("/q", -1),
    ),
)
def test_input_cicle_return_handler_result(
    search_setup, add_setup, mock_input, cmd_name, expected_handler_result
) -> None:
    mock_input(cmd_name)
    assert input_cicle(FILE_PATH) == expected_handler_result


def test_app_exit(mock_input, mock_os_dir) -> None:
    mock_input(c.EXIT_CMD)
    mock_os_dir()
    assert app() == -1
