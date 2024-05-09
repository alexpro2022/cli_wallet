import csv
import os
from typing import Any, Generator

from src.constants import CSV_HEADER, ENCODING, REPO_DIR_NAME, REPO_FILE_NAME
from src.types import Row


def create_repository(
    dir_name: str = REPO_DIR_NAME, file_name: str = REPO_FILE_NAME
) -> str:
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass
    file_path = os.path.join(os.getcwd(), dir_name, file_name)
    if not os.path.exists(file_path):
        write_csv(file_path, CSV_HEADER)
    return file_path


def write_csv(file_path: str, row: Row, mode: str = "a") -> None:
    with open(file_path, mode, **ENCODING) as csv_file:  # type: ignore [call-overload]
        writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        writer.writerow(row)


def read_csv(file_path: str) -> Generator[Row, Any, None]:
    with open(file_path, "r", **ENCODING) as file:  # type: ignore [call-overload]
        yield from csv.reader(file)
