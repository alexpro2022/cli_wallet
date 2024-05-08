from decimal import Decimal

from src.constants import BALANCE, CREDIT, DEBIT
from src.repository import read_csv, write_csv
from src.types import Rows
from src.utils import get_today
from src.validators import get_valid_category, get_valid_decimal


def edit_record(file_path: str) -> None: ...


def add_record(file_path: str) -> str:
    date = get_today()
    category = get_valid_category(input, "Введите категорию: ")
    value = get_valid_decimal(input, "Введите сумму: ")
    description = input("Введите описание: ")
    write_csv(file_path, [date, category, str(value), description])
    return "Запись добавлена."


def search_record(file_path: str, search_value: str | None = None) -> Rows:
    if search_value is None:
        search_value = input("Введите искомое значение: ")
        print("Найденные элементы: ")
    return [row for row in read_csv(file_path) if search_value in row]


def balance(file_path: str) -> tuple[str, str, str]:
    def _sum(rows: Rows):
        return sum(map(Decimal, [row[2] for row in rows]))

    def _f(name: str, value: Decimal) -> str:
        return f"{name}: {value}"

    debit = _sum(search_record(file_path, search_value=DEBIT))
    credit = _sum(search_record(file_path, search_value=CREDIT))
    balance = debit - credit
    return _f(BALANCE, balance), _f(DEBIT, debit), _f(CREDIT, credit)
