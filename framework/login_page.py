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

    def return_to_main_page(self):
        self.find_element(
            '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
        ).click()
        self.find_element(
            '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="App Settings"]'
        ).click()
        self.find_element(
            '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Sign Out"]'
        ).click()

    def click_go_back_button(self):
        self.find_element(
            '//android.widget.ImageButton[@resource-id="com.ajaxsystems:id/back"]'
        ).click()
