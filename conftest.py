import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def driver():
    """Фикстура с headless Chrome через Selenium Manager"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # Selenium Manager сам скачает нужный ChromeDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    yield driver
    driver.quit()