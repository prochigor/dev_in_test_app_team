import pytest

from framework.login_page import LoginPage
from tests.conftest import driver, run_appium_server


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield LoginPage(driver)
