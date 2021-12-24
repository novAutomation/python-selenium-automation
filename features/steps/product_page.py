
from selenium.webdriver.common.by import By
from behave import then, when, given

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {product_id} page')
def open_amazon_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')


@then('Verify User clicks through colors')
def verify_user_clicks_colors(context):
    expected_colors = ['Army Green', 'Black', 'Blue', 'Brown', 'Burgundy', 'Caramel', 'Dark Blue', 'Denim Blue', 'Gray',
                       'Green', 'Khaki', 'Light-green', 'Pink', 'Purple', 'Red', 'Rose Red', 'White', 'Yellow']

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for i in range (len(colors)):
        colors[i].click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text
        print(actual_color)

        assert actual_color == expected_colors[i], f'Expected {expected_colors[i]} but got {actual_color}'
