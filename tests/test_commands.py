import pytest

from src.commands import Command, Commands


@pytest.mark.parametrize("attr", ("name", "description", "handler"))
def test_class_command(attr) -> None:
    assert hasattr(Command("", "", lambda: ...), attr)


@pytest.mark.parametrize(
    "attr", ("balance", "add_record", "edit_record", "search_record", "exit")
)
def test_class_commands(attr) -> None:
    assert hasattr(Commands, attr)
