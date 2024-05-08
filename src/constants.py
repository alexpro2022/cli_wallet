DESCR_FLAG = "d"
EXIT_CMD = "exit"
EXIT_CMD_DESCR = "Выход из приложения."
BALANCE_CMD = "balance"
BALANCE_CMD_DESCR = (
    "Вывод баланса: Показать текущий баланс, а также отдельно доходы и расходы."
)
ADD_CMD = "add"
ADD_CMD_DESCR = (
    "Добавление записи: Возможность добавления новой записи о доходе или расходе."
)
EDIT_CMD = "edit"
EDIT_CMD_DESCR = (
    "Редактирование записи: Изменение существующих записей о доходах и расходах."
)
SERACH_CMD = "search"
SERACH_CMD_DESCR = "Поиск по записям: Поиск записей по категории, дате или сумме."
INPUT_MSG = (
    f"Введите команду [{BALANCE_CMD}, {ADD_CMD}, {EDIT_CMD}, {SERACH_CMD}, {EXIT_CMD}] "
    f"флаг -{DESCR_FLAG} описание команды:"
)
HELP_MSG = f"Неизвестная команда - {INPUT_MSG}"

REPO_DIR_NAME = "data"
REPO_FILE_NAME = "data.csv"
