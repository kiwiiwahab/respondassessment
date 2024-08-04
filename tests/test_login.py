# tests/test_login.py
from pageObjects.login_page import LoginPage


def test_verified_email_login(browser, user_data):
    login_page = LoginPage(browser)

    # Load the login page
    login_page.load()

    # Fill the login form with test data
    login_page.fill_login_form(
        user_data["email"],
        user_data["password"]
    )
    assert (login_page.successful_login_verified_email()), f"Login Failed"
