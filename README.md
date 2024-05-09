# cli_wallet

[![Test Suite](https://github.com/alexpro2022/cli_wallet/actions/workflows/branch_test.yml/badge.svg)](https://github.com/alexpro2022/cli_wallet/actions/workflows/branch_test.yml)



1. Создайте и активируйте виртуальное окружение и установите необходимые зависимости::
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

2. Из корневой директории проекта выполните команду:
```bash
pytest --cov --cov-config=.coveragerc
```


2. Из корневой директории проекта выполните команду:
```bash
python main.py
```
