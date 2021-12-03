from selenium.webdriver.common.by import By
from behave import *
from time import sleep


@then('Ipad added to Cart')
def verify_ipad_added(context):
    sleep(4)
    actual_text = context.driver.find_element(By.XPATH, "//div[@id='huc-v2-order-row-confirm-text']/h1").text
    expected_text = "Added to Cart"

    assert expected_text == actual_text, f' Error!, expected: {expected_text} but got: {actual_text}'

