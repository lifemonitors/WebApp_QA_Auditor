from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from webapp.locators.registration_locators import RegistrationLocators

class RegistrationPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*RegistrationLocators.USERNAME_INPUT).send_keys(username)

    def enter_email(self, email):
        self.driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)

    def click_register(self):
        self.driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()
