import pytest
from webapp.pages.registration_page import RegistrationPage
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_successful_registration(driver):
    page = RegistrationPage(driver)
    page.open()
    page.fill_registration_form(
        username="new_user",
        email="new_user@example.com",
        password="StrongPass123"
    )
    page.submit()
    assert page.success_message_is_displayed()
