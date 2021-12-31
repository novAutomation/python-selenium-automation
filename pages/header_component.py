from selenium.webdriver.common.by import By
from pages.base_page import Page


class HeaderComponent(Page):
    ORDERS_LOCATOR = (By.ID, 'nav-orders')
    CART_COUNT = (By.CSS_SELECTOR, '#nav-cart-count-container')

    def click_orders(self, *locator):
        self.click(*self.ORDERS_LOCATOR)

    def click_cart(self, *locator):
        self.click(*self.CART_COUNT)