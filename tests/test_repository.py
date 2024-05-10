from typing import Generator

import pytest

from src.constants import CSV_HEADER
from src.repository import (
    REPO_DIR_NAME,
    REPO_FILE_NAME,
    create_repository,
    read_csv,
    write_csv,
)
from tests.data import FILE_PATH


def mock_os_dir_raise_exc(*args, **kwargs):
    raise FileExistsError


@pytest.mark.parametrize("mock", (None, mock_os_dir_raise_exc))
@pytest.mark.parametrize("name", (REPO_DIR_NAME, REPO_FILE_NAME))
def test_create_repository_return_file_path(mock_os_dir, mock, name) -> None:
    mock_os_dir() if mock is None else mock_os_dir(mock_func=mock)
    assert create_repository().find(name) != -1


def test_create_repository_create_csv_file(mock_os_dir, mock_csv_writer) -> None:
    mock_os_dir(file_exists=False)
    assert isinstance(create_repository(), str)


def test_write_csv(mock_csv_writer) -> None:
    write_csv(FILE_PATH, CSV_HEADER)


def test_read_csv(monkeypatch, mock_open_file) -> None:
    monkeypatch.setattr("csv.reader", lambda _: range(10))
    reader = read_csv(FILE_PATH)
    assert isinstance(reader, Generator)
    counter = 0
    for row in reader:
        assert row == counter
        counter += 1
