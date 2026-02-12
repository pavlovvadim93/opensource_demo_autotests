from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
import allure

class DashboardPage(BasePage):
    DASHBOARD_HEADER = (By.CSS_SELECTOR, "h6.oxd-topbar-header-breadcrumb-module")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открылась страница 'Dashboard'")
    def is_dashboard_displayed(self) -> bool:
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.DASHBOARD_HEADER)
            )
            return True
        except:
            return False