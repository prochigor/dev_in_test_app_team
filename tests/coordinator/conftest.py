import pytest

from framework.coordinator_page import CoordinatorPage
from tests.conftest import driver, run_appium_server


@pytest.fixture(scope='function')
def user_side_bar_fixture(driver):
    yield CoordinatorPage(driver)
