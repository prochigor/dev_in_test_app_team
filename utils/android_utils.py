import logging
import subprocess

from framework.logging_config import configure_logging

configure_logging()


def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '14',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': get_udid(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }


def get_udid():
    adb_devices_output = subprocess.check_output(["adb", "devices"], encoding="utf-8")
    lines = adb_devices_output.strip().split('\n')

    if len(lines) > 1:
        udid = lines[1].split('\t')[0]
        logging.info(f"device udid: {udid}")
        return udid
    else:
        logging.error("device not found")
        return None
