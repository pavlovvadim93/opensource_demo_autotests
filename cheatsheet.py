"""
ШПАРГАЛКА по Selenium
"""
# 1. Основные методы драйвера:
driver.get("url")           # открыть страницу
driver.title                # заголовок страницы
driver.current_url          # текущий URL
driver.back()               # назад в истории
driver.forward()            # вперед в истории
driver.refresh()            # обновить страницу
driver.quit()               # закрыть браузер

# 2. Поиск элементов (возвращают WebElement):
driver.find_element(By.ID, "id")           # по ID
driver.find_element(By.NAME, "name")       # по имени
driver.find_element(By.XPATH, "//button")  # по XPATH
driver.find_element(By.CSS_SELECTOR, ".class") # по CSS

# 3. Что можно делать с элементом (WebElement):
element.click()                          # кликнуть
element.send_keys("text")                # ввести текст
element.clear()                          # очистить поле
element.is_displayed()                   # видим ли элемент
element.is_enabled()                     # доступен ли для взаимодействия
element.text                             # получить текст элемента
element.get_attribute("attribute_name")  # получить атрибут

# 4. Ожидания (WebDriverWait):
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
# Ждем появления элемента:
element = wait.until(EC.presence_of_element_located((By.ID, "id")))
# Ждем кликабельности:
element = wait.until(EC.element_to_be_clickable((By.ID, "id")))
# Ждем видимости:
element = wait.until(EC.visibility_of_element_located((By.ID, "id")))