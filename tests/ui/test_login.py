from utils.driver_factory import create_driver
from utils.logger import setup_logger

def test_successful_login():
    logger = setup_logger("login_test")
    driver = create_driver()
    logger.info("Открытие сайта")
    driver.get("https://www.saucedemo.com")

    logger.info("Ввод логина и пароля")
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    logger.info("Проверка, что вошли в систему")
    assert "inventory" in driver.current_url

    driver.quit()
