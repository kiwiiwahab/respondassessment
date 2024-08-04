# tests/test_signup.py
from pageObjects.signup_page import SignupPage


def test_signup(browser, user_data):
    signup_page = SignupPage(browser)

    # Load the signup page
    signup_page.load()

    # Fill the signup form with test data
    signup_page.fill_signup_form(
        user_data["first_name"],
        user_data["last_name"],
        user_data["email"],
        user_data["password"]
    )
    assert signup_page.verify_email_text_present(), f"Sign Up failed"


def test_duplicate_email(browser, user_data):
    signup_page = SignupPage(browser)

    # Load the signup page
    signup_page.load()

    # Fill the signup form with test data
    signup_page.fill_signup_form(
        user_data["first_name"],
        user_data["last_name"],
        user_data["email"],
        user_data["password"]
    )
    assert signup_page.duplicate_email(), f"Email Duplication"


