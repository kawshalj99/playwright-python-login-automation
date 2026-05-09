Playwright Python Login Automation

This project demonstrates a simple login page automation framework using:

* Playwright
* python
* Pytest
* Page Object Model (POM)

Covered Scenarios:

* Valid login
* Invalid login
* Empty username
* Empty password
* Empty fields validation

Project Structure:

    playwright_login_test/
    |
    |--pages/
    |  |--login_page.py
    |
    |--tests/
    |   |--test_login.py
    |
    |--conftest.py
    |__requirements.txt

Run the project

Install dependencies:

* pip install -r requirements.txt

Install Playwright browsers:

* playwright install

Run tests:

* pytest -v

