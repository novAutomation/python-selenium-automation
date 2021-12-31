from selenium.webdriver.common.by import By
from pages.base_page import Page


class VerifyCartEmpty(Page):

    EMPTY_CART_TEXT = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

    def verify_empty_cart(self, expected_text):
        self.verify_text(expected_text, *self.EMPTY_CART_TEXT)