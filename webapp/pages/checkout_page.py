class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://your-webapp.com/checkout")

    def add_items_to_cart(self):
        self.driver.find_element("id", "add-item-1").click()
        self.driver.find_element("id", "add-item-2").click()

    def proceed_to_checkout(self):
        self.driver.find_element("id", "checkout-button").click()

    def confirmation_is_displayed(self):
        return "order confirmed" in self.driver.page_source.lower()
