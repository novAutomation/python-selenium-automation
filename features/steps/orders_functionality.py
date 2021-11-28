import time
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('User launch Amazon application')
def launch_application(context):
    context.driver.get('https://www.amazon.com')
    time.sleep(1)
@when('User clicks Orders tab')
def click_orders_tab(context):
    context.driver.find_element(By.XPATH, "//a[@href = '/gp/css/order-history?ref_=nav_orders_first']").click()
    time.sleep(1)
@then('Sign In page is displayed')
def verify_sign_in_page(context):
    expected_text = 'Sign-In'
    actual_text = context.driver.find_element(By.XPATH, "//*[@class = 'a-spacing-small']").text
    assert expected_text == actual_text, f'Expected text: {expected_text}, but actual text: {actual_text}'
    print(f'***********************')
    print(f'This is the {actual_text} Page')
    time.sleep(1)
    context.driver.quit()
