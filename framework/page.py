from appium.webdriver.common.appiumby import AppiumBy


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, value):
        element = self.driver.find_element(by=AppiumBy.XPATH, value=value)
        return element

    @staticmethod
    def click_element(element):
        element.click()
