import pytest
from pages.login_page import LoginPage


def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("validUser", "validPass")

    assert login_page.is_dashboard_visible()


@pytest.mark.parametrize("username,password,expected_error", [
    ("wrongUser", "wrongPass", "Invalid credentials"),
    ("", "password123", "Username is required"),
    ("validUser", "", "Password is required"),
    ("", "", "Username is required"),
])

def test_invalid_login(page, username, password, expected_error):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(username, password)

    assert expected_error in login_page.get_error_message()