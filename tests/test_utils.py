import pytest

from src.utils import REPO_DIR_NAME, REPO_FILE_NAME, create_repository, parse


@pytest.mark.parametrize(
    "input, expected",
    (
        ("cmd-flag", ["cmd", "flag"]),
        (" cmd - flag ", ["cmd", "flag"]),
        ("cmd", ["cmd", ""]),
    ),
)
def test_parse(input, expected) -> None:
    assert parse(input) == expected


def mock_os_dir_raise_exc(*args, **kwargs):
    raise FileExistsError


@pytest.mark.parametrize("mock", (None, mock_os_dir_raise_exc))
@pytest.mark.parametrize("name", (REPO_DIR_NAME, REPO_FILE_NAME))
def test_create_repository(monkeypatch, mock_os_dir, mock, name) -> None:
    mock_os_dir() if mock is None else mock_os_dir(mock)
    assert create_repository().find(name) != -1
