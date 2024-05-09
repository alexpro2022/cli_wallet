CATEGORIES = ("доход", "расход")

DESCR_FLAG = "d"

# COMMANDS
BALANCE_CMD = "balance"  # also /b
ADD_CMD = "add"
EDIT_CMD = "edit"
SEARCH_CMD = "search"
EXIT_CMD = "exit"
UP_CMD = "/u"
DOWN_CMD = "/d"

# DESCRIPTIONS
BALANCE_CMD_DESCR = (
    "Вывод баланса: Показать текущий баланс, а также отдельно доходы и расходы."
)
ADD_CMD_DESCR = (
    "Добавление записи: Возможность добавления новой записи о доходе или расходе."
)

EDIT_CMD_DESCR = (
    "Редактирование записи: Изменение существующих записей о доходах и расходах."
)
SEARCH_CMD_DESCR = "Поиск по записям: Поиск записей по категории, дате или сумме."
EXIT_CMD_DESCR = "Выход из приложения."

# MESSAGES
INPUT_MSG = (
    f"Введите команду [/b-{BALANCE_CMD}, /a-{ADD_CMD}, "
    f"/e-{EDIT_CMD}, /s-{SEARCH_CMD}, /q-{EXIT_CMD}] "
    f"флаг -{DESCR_FLAG} описание команды: "
)
HELP_MSG = f"Неизвестная команда - {INPUT_MSG}."
TRY_AGAIN_MSG = ", попробуйте еще раз: "
DECIMAL_INPUT_ERR_MSG = f"Ожидается ввод числа{TRY_AGAIN_MSG}"
CATEGORY_INPUT_ERR_MSG = (
    f"Ожидается ввод одного из вариантов " f"из {CATEGORIES}{TRY_AGAIN_MSG}"
)
SOMETHING_WRONG_MSG = f"Что то пошло не так{TRY_AGAIN_MSG}"
RECORD_SAVED_MSG = "Запись сохранена в файл."
EDIT_MSG = (
    "Введите номер строки для редактирования, либо команды "
    "/u /d для скроллинга вверх-вниз соответственно: "
)
NO_SCROLL_UP_MSG = "Достигнуто начало таблицы. Скроллинг вверх невозможен: "
NO_SCROLL_DOWN_MSG = "Достигнут конец таблицы. Скроллинг вниз невозможен: "
INPUT_NEW_DATA_MSG = (
    "Введите через пробел название_столбца новое_значение. (Выход - /q): "
)

# REPOSITORY
REPO_DIR_NAME = "data"
REPO_FILE_NAME = "data.csv"
ENCODING = {"encoding": "utf-8"}
CSV_HEADER = "Дата,Категория,Сумма,Описание".split(",")


DEBIT = "доход"
CREDIT = "расход"
BALANCE = "баланс"

PAGINATION = 3
