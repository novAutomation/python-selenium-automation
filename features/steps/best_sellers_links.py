from selenium.webdriver.common.by import By
from behave import given, when, then


BEST_SELLERS_LINKS = (By.CSS_SELECTOR, 'div#nav-xshop-container a')


@given('User open Amazon Best Sellers Page')
def user_open_amazon_best_seller_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('User verify {expected_count} links')
def user_verify_links_count(context, expected_count):
    expected_count = int(expected_count)
    links_count = context.driver.find_elements(*BEST_SELLERS_LINKS)
    assert len(links_count) == expected_count, f'Error! Expected 30 Links but got {len(links_count)} Links'