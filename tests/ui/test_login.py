import pytest
from selenium import webdriver
from webapp.pages.login_page import LoginPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_login(driver):
    page = LoginPage(driver)
    page.load("https://example.com/login")  # заменить на нужный URL
    page.login("demo_user", "demo_pass")
    assert "dashboard" in driver.current_url  # пример проверки
