import logging
import time
import pytest

from tests.login.conftest import user_login_fixture
from framework.logging_config import configure_logging

configure_logging()


@pytest.mark.parametrize(
    "login,password",
    [
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            id="should log in with correct login and password"
        ),
        pytest.param(
            " qa.ajax.app.automation@gm ail.com ",
            "qa_automation_password",
            id="should log in for login with spaces and correct password"
        ),
    ]
)
def test_user_login(login, password, user_login_fixture):
    logging.info("Opening login page...")
    user_login_fixture.click_login_button()
    logging.info("login page is successfully opened")
    logging.info(f"Logging in with login: {login}, password: {password}")
    user_login_fixture.perform_login(login, password)
    logging.info("successfully logged in")
    time.sleep(6)

    assert user_login_fixture.is_login_successful()

    logging.info("Returning to base page...")
    user_login_fixture.return_to_main_page()
    logging.info("Successfully returned to base page")
    time.sleep(5)


@pytest.mark.parametrize(
    "login,password,error_message",
    [
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_1password",
            "Wrong login or password",
            id="shouldn't log in with incorrect password"
        ),
        pytest.param(
            "qc.ajax.app.failed@gmail.com",
            "qa_automation_password",
            "Wrong login or password",
            id="shouldn't log in with incorrect login"
        ),
        pytest.param(
            "qc.ajax.app",
            "qa_automation_password",
            "Invalid email format",
            id="shouldn't log in with invalid email"
        ),
    ]
)
def test_user_wrong_login(login, password, error_message, user_login_fixture):
    logging.info("Opening login page...")
    user_login_fixture.click_login_button()
    logging.info("login page is successfully opened")
    time.sleep(1)
    logging.info(f"Logging in with login: {login}, password: {password}")
    user_login_fixture.perform_login(login, password)
    logging.info("successfully not logged in")
    time.sleep(2)
    error = user_login_fixture.find_element(
        '//android.widget.TextView[@resource-id="com.ajaxsystems:id/snackbar_text"]'
    )
    assert error.text == error_message
    assert user_login_fixture.is_login_failed()

    logging.info("Returning to base page...")
    user_login_fixture.click_go_back_button()
    logging.info("Successfully returned to base page")


@pytest.mark.parametrize(
    "login,password",
    [
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "",
            id="login button shouldn't displayed with empty field password"
        ),
        pytest.param(
            "",
            "qa_automation_password",
            id="login button shouldn't displayed with empty field login"
        ),
    ]
)
def test_user_empty_login_field(login, password, user_login_fixture):
    logging.info("Opening login page...")
    user_login_fixture.click_login_button()
    logging.info("login page is successfully opened")
    time.sleep(1)
    logging.info(f"Logging in with login: {login}, password: {password}")
    user_login_fixture.perform_login(login, password)

    login_button = user_login_fixture.find_element(
        '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxs'
        'ystems:id/compose_view"])[4]/android.view.View/android.view.View/android.widget.Button'
    )
    logging.info("Button log in successfully disabled")

    assert login_button.get_attribute("clickable") == "false"

    logging.info("Returning to base page...")
    user_login_fixture.click_go_back_button()
    logging.info("Successfully returned to base page")
