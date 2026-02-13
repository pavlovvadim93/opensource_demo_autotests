from pages.login_page import LoginPage
import pytest
import allure

@allure.feature("Авторизация")
@allure.story("Негативный сценарий")
@pytest.mark.parametrize("password", ["wrong", "12345", "qadefef", "2313dd"])
def test_multiple_invalid_passwords(browser, password):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("Admin", password)
    
    error_text = login_page.get_error_message()
    assert error_text is not None, "Сообщение об ошибке не появилось"
    assert "Invalid credentials" in error_text