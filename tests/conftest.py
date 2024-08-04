import json
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def user_data():
    return {
        "first_name": "Kanwal",
        "last_name": "Wahab",
        "email": "janedoe@gmail.com",
        "password": "flutus122.A"
    }

