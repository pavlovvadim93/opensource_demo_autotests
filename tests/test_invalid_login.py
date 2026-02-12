from pages.login_page import LoginPage
import allure
import pytest

@allure.feature("Авторизация")
@allure.story("Негативный сценарий")
def test_invalid_login(browser):
    login_page = LoginPage(browser)
    login_page.open()

    login_page.login("Admin", "wrong_password")

    error_text = login_page.get_error_message()
    assert error_text != None, "Сообщение об ошибке не появилось"
    assert "Invalid credentials" in error_text, f"Неверный текст ошибки: {error_text}"







