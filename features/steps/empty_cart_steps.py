from behave import given, when, then


@then("Verify 'Your Amazon Cart is empty' text present")
def verify_empty_cart_page(context):
    context.app.empty_cart_results_page.verify_empty_cart('Your Amazon Cart is empty')