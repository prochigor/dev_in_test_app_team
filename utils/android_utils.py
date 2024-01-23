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
        'udid': 'emulator-5554',
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
}
