import os

from src.constants import REPO_DIR_NAME, REPO_FILE_NAME


def parse(input: str) -> list[str]:
    inp: list[str] = list(map(lambda s: s.strip(), input.split("-")))
    if len(inp) == 1:
        inp.append("")
    return inp


def create_repository(
    dir_name: str = REPO_DIR_NAME, file_name: str = REPO_FILE_NAME
) -> str:
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass
    file_path = os.path.join(os.getcwd(), dir_name, file_name)
    if not os.path.exists(file_path):
        with open(file_path, "w") as fp:
            fp.write("Дата,Категория,Сумма,Описание")
    return file_path
