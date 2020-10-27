from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Test_Demo_04day.test_weixin_demo.page.register_page import RegisterPage


class LoginPage():

    def __init__(self,driver: WebDriver):
        self.driver = driver

    def scan(self):
        pass

    def goto_register(self):

        self.driver.find_element(By.CSS_SELECTOR,".login_registerBar_link").click()
        return RegisterPage(self.driver)