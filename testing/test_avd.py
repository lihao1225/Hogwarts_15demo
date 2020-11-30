from time import sleep

from appium import webdriver


class TestAvd:

    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            "avd": "android6"
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_avd(self):
        sleep(2)
