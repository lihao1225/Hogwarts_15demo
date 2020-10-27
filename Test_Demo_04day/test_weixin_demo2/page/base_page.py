from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""

    def __init__(self, driver: WebDriver = None):

        if driver == None:

            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(6)
            self.driver.maximize_window()

        else:
            self.driver = driver

        if self.base_url != "":
            self.driver.get(self.base_url)

    def find_ele(self, locator):
        return self.driver.find_element(*locator)

    def find_eles(self,locator):
        return self.driver.find_elements(*locator)

    def wait_for_click(self, locator, timeout=10):
        ele = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
        return ele
