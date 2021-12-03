
from selenium.webdriver.common.by import By
from behave import *


@then('Verify that Cancel Items or Orders text is present')
def verify_cancel_order_text(context):

    actual_text = context.driver.find_element(By.XPATH, "//div[@class = 'help-content']/h1").text
    expected_text = 'Cancel Items or Orders'

    assert expected_text == actual_text, f' Error!, expected {expected_text} but got: {actual_text}'

