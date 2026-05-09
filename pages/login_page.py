class LoginPage:
    def __init__(self, page):
        self.page = page

        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.locator("#loginBtn")

        self.error_message = page.locator(".error")
        self.dashboard = page.locator("#dashboard")

    def navigate(self):
        self.page.goto("http://localhost:5173")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.text_content()

    def is_dashboard_visible(self):
        return self.dashboard.is_visible()