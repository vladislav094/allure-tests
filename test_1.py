import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def browser():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(1)
    yield
    driver.quit()
    print('Test comletedse')

@allure.feature('Check')
@allure.story('Open site and type credentials')
@allure.severity('blocker')
def test_01(browser):
    driver.get("http://suninjuly.github.io/simple_form_find_task.html")
    first_field = driver.find_element(By.NAME, "first_name")
    first_field.send_keys("Ivan")
    last_field = driver.find_element(By.NAME, "last_name")
    last_field.send_keys("Petrov")
    city_field = driver.find_element(By.NAME, "firstname")
    city_field.send_keys("Smolensk")
    country_field = driver.find_element(By.ID, "country")
    country_field.send_keys("Russia")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

