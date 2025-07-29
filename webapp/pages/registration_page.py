from webapp.locators.registration_locators import RegistrationLocators

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = RegistrationLocators()

    def open(self):
        self.driver.get("https://your-webapp.com/register")

    def fill_registration_form(self, username, email, password):
        self.driver.find_element(*self.locators.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.locators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.locators.PASSWORD_INPUT).send_keys(password)

    def submit(self):
        self.driver.find_element(*self.locators.SUBMIT_BUTTON).click()

    def success_message_is_displayed(self):
        return "successfully" in self.driver.page_source.lower()
