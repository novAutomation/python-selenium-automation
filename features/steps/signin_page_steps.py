
from behave import *
from selenium.webdriver.common.by import By


@then('Verify Sign in page opened')
def verify_sign_in_page(context):

    context.driver.find_element(By.ID, 'ap_email')
    expected_header = 'Sign-In'
    actual_header = context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").text
    assert expected_header == actual_header, f'Error! Expected text: {expected_header}, but actual text: {actual_header}'


