from selenium.webdriver.common.by import By
from pages.base_page import Page


class VerifySignIn(Page):

    TEXT_HEADER = (By.CSS_SELECTOR, "h1.a-spacing-small")

    def verify_sign_in(self, expected_text):
        self.verify_text(expected_text, *self.TEXT_HEADER)
