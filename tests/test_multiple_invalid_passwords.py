from pages.login_page import LoginPage
import pytest
import allure

@allure.feature("Авторизация")
@allure.story("Негативный сценарий")
@pytest.mark.parametrize("password", ["wrong", "12345", "", "   "])
def test_multiple_invalid_passwords(browser, password):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("Admin", password)
    assert "Invalid credentials" in login_page.get_error_message()