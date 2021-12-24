
from behave import given, when, then
from selenium.webdriver.common.by import By

PRODUCTS = (By.XPATH, "//li[@class = 's-result-item' and .//span[contains(@class, 'prime-price')]]/div")
PRODUCT_NAME = (By.CSS_SELECTOR,"span.wfm-sales-item-card__product-name")


@given('Open Amazon Wholefoods page')
def open_wholefoods_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('Verify that every product has a text Regular')
def verify_regular_text(context):
    product_elements = context.driver.find_elements(*PRODUCTS)

    for product_element in product_elements:
        assert 'Regular' in product_element.text, f'Expected Regular to be in text but got {product_element.text}'

        product_name = product_element.find_element(*PRODUCT_NAME).text
        print(product_name)
        assert product_name, f'expected non-empty product name'

