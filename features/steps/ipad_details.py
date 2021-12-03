from selenium.webdriver.common.by import By
from behave import *


@then('Ipad details shown')
def verify_ipad_details_text(context):

    actual_text = context.driver.find_element(By.XPATH, "//div[@id='titleSection']/h1").text
    expected_text = "2021 Apple 10.2-inch iPad (Wi-Fi + Cellular, 256GB) - Space Gray"

    assert expected_text == actual_text, f' Error!, expected: {expected_text} but got: {actual_text}'

