import pytest
from webapp.pages.checkout_page import CheckoutPage
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_successful_checkout(driver):
    page = CheckoutPage(driver)
    page.open()
    page.add_items_to_cart()
    page.proceed_to_checkout()
    assert page.confirmation_is_displayed()
