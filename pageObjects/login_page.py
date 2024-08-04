# tests/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://app.respond.io/user/login"

    def load(self):
        self.browser.get(self.url)

    def fill_login_form(self, email, password):
        email_input = self.browser.find_element(By.NAME, "field_2")
        password_input = self.browser.find_element(By.NAME, "field_3")
        submit_button = self.browser.find_element(By.XPATH, "//button[@type='submit']")

        email_input.send_keys(email)
        password_input.send_keys(password)
        submit_button.click()

# Email verified but organization not set up
    def successful_login_verified_email(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="authContainer"]/div[1]/div[2]/div/div/div/div[2]/div/div')
        ))
        element = self.browser.find_element(By.XPATH, '//*[@id="authContainer"]/div[1]/div[2]/div/div/div/div[2]/div/div')
        return element.text == 'Provide your details to get started.'

