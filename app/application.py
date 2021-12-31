from pages.header_component import HeaderComponent
from pages.home_page import HomePage
from pages.verify_header_component import VerifySignIn
from pages.verify_empty_cart import VerifyCartEmpty


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.headerComponent = HeaderComponent(self.driver)
        self.homePage = HomePage(self.driver)
        self.sign_in_results_page = VerifySignIn(self.driver)
        self.empty_cart_results_page = VerifyCartEmpty(self.driver)