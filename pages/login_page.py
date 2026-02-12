from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):

    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    MESSAGE = (By.CSS_SELECTOR, "div[role='alert']")


    def __init__(self, driver):
        super().__init__(driver)

# КОМАНДЫ
    @allure.step("Открыть страницу логина")
    def open(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        print(f"Открываем сайт: {self.driver.current_url}")
        return self

    @allure.step("Ввести данные пользователя")
    def login_form(self, username: str, password: str):
        self.wait.until(
            EC.presence_of_element_located((self.USERNAME_FIELD))
        ).send_keys(username)
        self.wait.until(
            EC.presence_of_element_located((self.PASSWORD_FIELD))
        ).send_keys(password)
        print("Данные пользователя введены")
        return self

    @allure.step("Нажать кнопку 'Login'")
    def login_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.LOGIN_BUTTON))
        ).click()
        print("Нажата кнопка 'Login'")
        return self

    @allure.step("Ввести данные пользователя и нажать кнопку 'Login'")
    def login(self,username,password):
        self.login_form(username, password)
        self.login_button()
        from pages.dashboard_page import DashboardPage
        return DashboardPage(self.driver)

# ПРОВЕРКИ
    @allure.step("Появилась ошибка")
    def get_error_message(self) -> str | None:
        try:
            error = self.wait.until(
                EC.presence_of_element_located((self.MESSAGE))
            )

            return error.text
        except:
            return None
