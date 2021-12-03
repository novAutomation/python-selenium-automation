from selenium.webdriver.common.by import By
from behave import *


@then('User verifies that Amazon Cart is empty')
def verify_empty_cart_text(context):

    actual_text = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
    expected_text = 'Your Amazon Cart is empty'

    assert expected_text == actual_text, f' Error!, expected: {expected_text} but got: {actual_text}'

