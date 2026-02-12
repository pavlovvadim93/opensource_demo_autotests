from pages.login_page import LoginPage
import allure
import pytest

@allure.feature("Авторизация")
@allure.story("Позитивный сценарий")
def test_smoke(browser):
    login_page = LoginPage(browser)
    login_page.open()

    dashboard_page = login_page.login("Admin", "admin123")
    assert dashboard_page.is_dashboard_displayed(), "Дасшбоард не открылся"