# Selenium Tests for User Signup and Login

This repository contains Selenium-based automated tests for user signup and login functionalities of a web application. The tests are written using the pytest framework.

## Project Structure
- **tests/**: Contains the test files and page object classes.
  - **test_login.py**: Contains the test case for the login process.
  - **test_signup.py**: Contains the test case for the signup process.
  - **login_page.py**: Page object class for the login page.
  - **signup_page.py**: Page object class for the signup page.
  - **__init__.py**: Initializes the `tests` package.
- **conftest.py**: Contains pytest fixtures, including browser setup and teardown.


## Setup and Installation

### Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (Ensure it matches the installed version of Chrome)
- pip install pytest selenium

### Install Dependencies

Clone the repository:
   ```sh
   git clone https://github.com/kiwiiwahab/respondassessment.git
   cd respondassessment

   
### Run Tests
To run the tests, use the following command:
pytest --html=report.html -v -s

**Test Signup**
  test_signup.py
  Verifies the user signup functionality.
  Fills out the signup form with predefined user data.
  Asserts that the page contains the text "Verify your email" after form submission to confirm a successful signup.
**Test Login**
  test_login.py
  Verifies the user login functionality.
  Fills out the login form with predefined user credentials.
  Asserts successful login by checking for specific elements or text on the post-login page.

**Page Object Classes
****SignupPage**
signup_page.py: Methods to load the signup page, fill out the signup form, and verify the presence of specific texts or elements after form submission.
**LoginPage**
login_page.py: Methods to load the login page, fill out the login form, and verify the presence of specific texts or elements after form submission.


