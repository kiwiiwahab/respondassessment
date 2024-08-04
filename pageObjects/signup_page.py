# tests/signup_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://app.respond.io/user/register"

    def load(self):
        self.browser.get(self.url)

    def fill_signup_form(self, firstname, lastname, email, password):
        firstname_input = self.browser.find_element(By.NAME, "field_2")
        lastname_input = self.browser.find_element(By.NAME, "field_3")
        email_input = self.browser.find_element(By.NAME, "field_4")
        password_input = self.browser.find_element(By.NAME, "password")
        submit_button = self.browser.find_element(By.XPATH, "//button[@type='submit']")

        firstname_input.send_keys(firstname)
        lastname_input.send_keys(lastname)
        email_input.send_keys(email)
        password_input.send_keys(password)
        submit_button.click()

    def verify_email_text_present(self):
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "Open Gmail")
            )
        )
        element = self.browser.find_element(By.LINK_TEXT, "Open Gmail")
        return element.text == "Open Gmail"

    def duplicate_email(self):
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".text.elevation-1")
            )
        )
        element = self.browser.find_element(By.CSS_SELECTOR, ".text.elevation-1")
        return element.text == "Email already exists. Please Sign In with this email."
