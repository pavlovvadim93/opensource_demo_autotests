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
    """Фикстура для создания драйвера Chrome с надёжным headless-режимом для CI"""
    chrome_options = Options()

    # Базовые настройки
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")

    # Критически важные флаги для работы в CI (без них Chrome падает)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--disable-software-rasterizer")

    # Если мы в CI — включаем headless и фиксированный размер окна
    if os.getenv("CI") or os.getenv("GITHUB_ACTIONS"):
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")

    # Автоматическая установка драйвера
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.implicitly_wait(5)
    yield driver
    driver.quit()