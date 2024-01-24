import logging
import time

from appium.webdriver.common.appiumby import AppiumBy

from tests.coordinator.conftest import user_side_bar_fixture
from framework.logging_config import configure_logging

configure_logging()


def test_sidebar_settings(user_side_bar_fixture):
    driver = user_side_bar_fixture.driver

    if user_side_bar_fixture.check_logged_in():
        user_side_bar_fixture.log_in()
        logging.info("successfully logged in")

    user_side_bar_fixture.open_sidebar()

    driver.find_element(by=AppiumBy.ID, value="com.ajaxsystems:id/settings").click()
    logging.info("settings successfully opened")

    element = driver.find_element(by=AppiumBy.ID, value="com.ajaxsystems:id/body")
    assert element.text == "qa.ajax.app.automation@gmail.com"

    driver.back()


def test_sidebar_help(user_side_bar_fixture):
    driver = user_side_bar_fixture.driver

    if user_side_bar_fixture.check_logged_in():
        user_side_bar_fixture.log_in()
        logging.info("successfully logged in")

    user_side_bar_fixture.open_sidebar()
    driver.find_element(by=AppiumBy.ID, value="com.ajaxsystems:id/help").click()
    time.sleep(3)
    logging.info("help page successfully opened")

    element = driver.find_element(
        by=AppiumBy.ID,
        value="com.ajaxsystems:id/toolbarTitle"
    )
    assert element.text == "Installation Manuals"

    driver.back()


def test_sidebar_report(user_side_bar_fixture):
    driver = user_side_bar_fixture.driver

    if user_side_bar_fixture.check_logged_in():
        user_side_bar_fixture.log_in()
        logging.info("successfully logged in")

    user_side_bar_fixture.open_sidebar()
    driver.find_element(by=AppiumBy.ID, value="com.ajaxsystems:id/logs").click()
    logging.info("Report a problem successfully opened")

    element = user_side_bar_fixture.find_element(
        '//android.widget.TextView[@resource-id="com.'
        'ajaxsystems:id/title" and @text="Report a Problem"]'
    )
    assert element.text == "Report a Problem"

    driver.back()


def test_sidebar_add_hub(user_side_bar_fixture):
    if user_side_bar_fixture.check_logged_in():
        user_side_bar_fixture.log_in()
        logging.info("successfully logged in")

    user_side_bar_fixture.open_sidebar()
    user_side_bar_fixture.find_element('//android.widget.Button').click()
    logging.info("Add hub page successfully opened")

    element = user_side_bar_fixture.find_element(
        '//android.widget.TextView[@resource-id="com'
        '.ajaxsystems:id/text" and @text="Use Wizard"]'
    )
    assert element.text == "Use Wizard"
    user_side_bar_fixture.driver.back()


def test_sidebar_term_of_service(user_side_bar_fixture):
    if user_side_bar_fixture.check_logged_in():
        user_side_bar_fixture.log_in()
        logging.info("successfully logged in")

    user_side_bar_fixture.open_sidebar()

    user_side_bar_fixture.find_element(
        '//android.widget.TextView[@resource-id="com'
        '.ajaxsystems:id/documentation_text"]'
    ).click()
    logging.info("Add hub page successfully opened")
    time.sleep(1)

    element = user_side_bar_fixture.find_element(
        '//android.widget.TextView[@resource-id="com.ajaxsystems:id/toolbarTitle"]'
    )
    assert element.text == "Terms of Service"
    user_side_bar_fixture.driver.back()


def test_sidebar_term_of_version(user_side_bar_fixture):
    if user_side_bar_fixture.check_logged_in():
        user_side_bar_fixture.log_in()
        logging.info("successfully logged in")

    user_side_bar_fixture.open_sidebar()

    element = user_side_bar_fixture.find_element(
        '//android.widget.TextView[@resource-id="com.ajaxsystems:id/build"]'
    )
    assert element.text == "v 2.34 (build #3749)"
