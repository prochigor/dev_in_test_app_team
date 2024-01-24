import time
from appium.webdriver.common.appiumby import AppiumBy

from framework.login_page import LoginPage


class CoordinatorPage(LoginPage):

    def open_sidebar(self):
        self.find_element(
            '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
        ).click()

    def log_in(self):
        login = "qa.ajax.app.automation@gmail.com"
        password = "qa_automation_password"

        self.click_login_button()
        self.perform_login(login, password)
        time.sleep(6)

    def check_logged_in(self):
        elements = self.driver.find_elements(
            by=AppiumBy.XPATH,
            value='//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]'
        )
        return len(elements) > 0
