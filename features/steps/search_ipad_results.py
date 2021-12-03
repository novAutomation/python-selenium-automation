
from selenium.webdriver.common.by import By
from behave import *


@then('Search results for Ipad shown')
def verify_ipad_search_text(context):

    actual_text = context.driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-small a-spacing-top-small']/span[@class='a-color-state a-text-bold']").text
    expected_text = '"Ipad"'

    assert expected_text == actual_text, f' Error!, expected {expected_text} but got: {actual_text}'

