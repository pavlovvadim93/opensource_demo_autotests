# OrangeHRM Automation Tests

![Tests Status](https://github.com/pavlovvadim93/orangehrm-autotests/actions/workflows/run_tests.yml/badge.svg)

Проект с автотестами для OrangeHRM (Selenium + Python + Pytest + PageObject).

## Стек технологий
- Python 3.10
- Selenium WebDriver
- Pytest
- PageObject
- Allure Reports
- GitHub Actions (CI)

## Запуск тестов локально
1. Установи зависимости: `pip install -r requirements.txt`
2. Запусти: `pytest tests/ -v`

## CI/CD
При каждом пуше в main тесты автоматически запускаются на GitHub Actions.