from dataclasses import dataclass

DESCR_FLAG = "-d"
INPUT_MSG = (
    f"Введите команду (balance, add, edit, search) флаг {DESCR_FLAG} описание команды:"
)
HELP_MSG = f"Неизвестная команда - {INPUT_MSG}"


@dataclass
class Command:
    name: str
    description: str


class Commands:
    balance = Command(
        "balance",
        "Вывод баланса: Показать текущий баланс, а также отдельно доходы и расходы.",
    )
    add_record = Command(
        "add",
        "Добавление записи: Возможность добавления новой записи о доходе или расходе.",
    )
    edit_record = Command(
        "edit",
        "Редактирование записи: Изменение существующих записей о доходах и расходах.",
    )
    search_record = Command(
        "search", "Поиск по записям: Поиск записей по категории, дате или сумме."
    )


def get_description(cmd: str) -> None:
    match cmd:
        case Commands.balance.name:
            print(Commands.balance.description)
        case Commands.add_record.name:
            print(Commands.add_record.description)
        case Commands.edit_record.name:
            print(Commands.edit_record.description)
        case Commands.search_record.name:
            print(Commands.search_record.description)
        case _:
            print(HELP_MSG)


def balance() -> None: ...
def add_record() -> None: ...
def edit_record() -> None: ...
def search_record() -> None: ...


handlers = {
    Commands.balance.name: balance,
    Commands.add_record.name: add_record,
    Commands.edit_record.name: edit_record,
    Commands.search_record.name: search_record,
}


def parse(input: str) -> list[str]:
    inp: list[str] = list(map(lambda s: s.strip(), input.split("-")))
    if len(inp) == 1:
        inp.append("")
    return inp


def main() -> None:
    while True:
        cmd, flag = parse(input(INPUT_MSG))
        if flag == "d":
            get_description(cmd)
        else:
            print("handlers")
            handlers.get(cmd)


if __name__ == "__main__":
    main()
