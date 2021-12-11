from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Ipad added to Cart')
def verify_ipad_added(context):
    sleep(4)
    actual_text = context.driver.find_element(By.XPATH, "//div[@class = 'a-section a-spacing-none a-padding-none sw-atc-productmessage'] "
                                                        "//span[@class='a-size-medium-plus a-color-base sw-atc-text a-text-bold']").text
    expected_text = "Added to Cart"
    assert expected_text == actual_text, f' Error!, expected: {expected_text} but got: {actual_text}'

