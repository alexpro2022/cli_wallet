# cli_wallet

[![Test Suite](https://github.com/alexpro2022/cli_wallet/actions/workflows/branch_test.yml/badge.svg)](https://github.com/alexpro2022/cli_wallet/actions/workflows/branch_test.yml)
[![codecov](https://codecov.io/gh/alexpro2022/cli_wallet/graph/badge.svg?token=81RgzLVrpG)](https://codecov.io/gh/alexpro2022/cli_wallet)

<br>

[Консольное приложение "Личный финансовый кошелек"](https://docs.google.com/document/d/1IszyY0--qsbBdgRVcfQXDloJDtvnKW4QsS7xQg2IpY8/edit)

<br>

## Оглавление
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка приложения](#установка-приложения)
- [Запуск тестов](#запуск-тестов)
- [Запуск приложения](#запуск-приложения)
- [Удаление приложения](#удаление-приложения)
- [Автор](#автор)

<br>

## Технологии
<details><summary>Подробнее</summary><br>

[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python)](https://www.python.org/)
[![csv](https://img.shields.io/badge/-csv-464646?logo=python)](https://docs.python.org/3/library/csv.html)
[![Pandas](https://img.shields.io/badge/-pandas-464646?logo=pandas)](https://pandas.pydata.org/docs/)
[![Pytest](https://img.shields.io/badge/-pytest-464646?logo=Pytest)](https://docs.pytest.org/en/latest/)
[![pytest-cov](https://img.shields.io/badge/-pytest--cov-464646?logo=codecov)](https://pytest-cov.readthedocs.io/en/latest/)
[![pre-commit](https://img.shields.io/badge/-pre--commit-464646?logo=pre-commit)](https://pre-commit.com/)

[⬆️Оглавление](#оглавление)

</details>

<br>

## Описание работы:
Данные хранятся в текстовом csv-файле, формат которого выбран разработчиком (условие ТЗ).
Управление осуществляется при помощи консольных команд, которые могут быть написаны в полном и сокращенном форматах.
<br>
Основные возможности приложения:
1. Вывод баланса: Показывает текущий баланс, а также отдельно доходы и расходы.
   Команды: `balance`  `/b`
2. Добавление записи: Возможность добавления новой записи о доходе или расходе.
   Команды: `add`  `/a`
3. Редактирование записи: Изменение существующих записей о доходах и расходах.
   Команды: `edit`  `/e`
4. Поиск по записям: Поиск записей по категории, дате или сумме.
   Команды: `search`  `/s`
5. Выход из приложения (<a href="#t2">Смотри ниже</a>):
   Команды: `exit`  `/q` (stands for `quit` as the `/e` is occupiied:)
<br>
Также предусмотрен флаг `-d` (description - выводит в консоль описание команды - аналог флагов -h --help в продуктовых разработках)
Примеры: `/a-d` или `add-d`


[⬆️Оглавление](#оглавление)

<br>

## Установка приложения:

1. Клонируйте репозиторий с GitHub:

```bash
git clone https://github.com/alexpro2022/cli_wallet.git
cd cli_wallet
```

2. Создайте и активируйте виртуальное окружение и установите необходимые зависимости::
   * Если у вас Linux/macOS
   ```bash
    python -m venv venv && source venv/bin/activate
    python -m pip install --upgrade pip && pip install -r requirements/test.requirements.txt
   ```
   * Если у вас Windows
   ```bash
    python -m venv venv && source venv/Scripts/activate
    python -m pip install --upgrade pip && pip install -r requirements/test.requirements.txt
   ```

[⬆️Оглавление](#оглавление)

<br>

## Запуск тестов:
Из корневой директории проекта выполните команду:
```bash
pytest --cov
```

[⬆️Оглавление](#оглавление)

<br>

## Запуск приложения:
1. Из корневой директории проекта выполните команду:
```bash
python main.py
```

2. Для <a href="#t2">остановки</a> можно использовать
  - либо cli-команду `/q` (возможно два раза в зависимрсти от уровня вызова команды)
  - либо сочетание клавиш `Ctrl-C`

[⬆️Оглавление](#оглавление)

<br>

## Удаление приложения:
Из корневой директории проекта выполните команду:
```bash
cd .. && rm -fr cli_wallet && deactivate
```

[⬆️Оглавление](#оглавление)

<br>

## Автор:
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#cli_wallet)
