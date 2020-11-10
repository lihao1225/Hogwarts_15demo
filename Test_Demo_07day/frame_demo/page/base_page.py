import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from Test_Demo_07day.frame_demo.common.handle_black import handle_black


class BasePage:
    black_list = [(By.XPATH, "//*[@resource-id = 'com.xueqiu.android:id/iv_close']")]
    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):

        if driver is None:
            desire_cap = {
                "platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "noReset": True
            }

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
            self.driver.implicitly_wait(10)

        else:
            self.driver = driver

    @handle_black
    def find(self, by, locator):

        if locator is None:
            result = self.driver.find_element(*by)

        else:
            result = self.driver.find_element(by, locator)

        return result

    def parse_yaml(self, path, func_name):
        """

        读取yaml的nr
        :param path:
        :param func_name:
        :return:
        """
        with open(path, encoding="utf-8") as f:
            data = yaml.load(f)
        self.parse(data[func_name])

    def parse(self, steps):
        """
        解析yaml
        :param steps:
        :return:
        """
        #遍历每一个步骤
        for step in steps:
            if "click" == step["action"]:
                self.find(step['by'], step['locator']).click()
            elif 'send_key' == step['action']:
                self.find(step['by'],step['locator']).send_keys(step['text'])
