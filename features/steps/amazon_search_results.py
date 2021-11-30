from behave import *
from selenium.webdriver.common.by import By


@then('Search results for table shown')
def search_results(context):
    expected_text = '"table"'
    actual_text = context.driver.find_element(By.XPATH, "//span[@class = 'a-color-state a-text-bold']").text
    assert expected_text == actual_text, f'Error! Expected text: {expected_text}, but actual text: {actual_text}'

