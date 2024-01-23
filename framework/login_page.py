from framework.page import Page


class LoginPage(Page):

    def perform_login(self, username, password):
        username_field = self.find_element(
            '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]'
        )
        password_field = self.find_element(
            '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]'
        )

        username_field.clear()
        username_field.send_keys(username)
        password_field.send_keys(password)

        self.click_login_button()

    def click_login_button(self):
        login_button = self.find_element(
                '//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]'
        )
        self.click_element(login_button)

    def is_login_successful(self):
        return self.find_element('//android.view.ViewGroup[@resource-id="com.ajaxsystems:id/hubAdd"]')

    def is_login_failed(self):
        return self.find_element('//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]')
