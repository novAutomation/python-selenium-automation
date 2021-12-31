
from behave import given, when, then


@then('Verify Sign in page opened')
def verify_sign_in_page(context):
    context.app.sign_in_results_page.verify_sign_in('Sign-In')


