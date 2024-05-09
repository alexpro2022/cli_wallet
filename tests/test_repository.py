import csv
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
def test_create_repository(mock_os_dir, mock, name) -> None:
    mock_os_dir() if mock is None else mock_os_dir(mock)
    assert create_repository().find(name) != -1


def test_write_csv(monkeypatch, mock_open_file) -> None:
    def mock_csv_writer(file, quoting, lineterminator):
        class _writer:
            @staticmethod
            def writerow(row):
                assert row == CSV_HEADER

        assert quoting == csv.QUOTE_MINIMAL
        assert lineterminator == "\n"
        return _writer()

    monkeypatch.setattr("csv.writer", mock_csv_writer)
    write_csv(FILE_PATH, CSV_HEADER)


def test_read_csv(monkeypatch, mock_open_file) -> None:
    monkeypatch.setattr("csv.reader", lambda _: range(10))
    reader = read_csv(FILE_PATH)
    assert isinstance(reader, Generator)
    counter = 0
    for row in reader:
        assert row == counter
        counter += 1
