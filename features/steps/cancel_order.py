
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from behave import *


@given('Open Amazon Help page')
def open_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html ')


@when('Search for Cancel Order & hit enter')
def search_for_cancel_order(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order', Keys.ENTER)


