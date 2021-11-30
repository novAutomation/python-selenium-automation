
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Search for table')
def search_table(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')


@when('Click search icon')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()