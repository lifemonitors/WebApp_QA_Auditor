from selenium import webdriver
import yaml

def create_driver():
    with open("config/settings.yaml", "r") as f:
        config = yaml.safe_load(f)

    browser = config.get("browser", "chrome")
    headless = config.get("headless", False)

    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(config.get("implicit_wait", 5))
    return driver
