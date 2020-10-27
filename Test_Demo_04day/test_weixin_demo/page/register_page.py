from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:

    def __init__(self,driver : WebDriver):
        self.driver = driver

    #注册信息
    def register_successful(self):
        self.driver.find_element(By.ID,"corp_name").send_keys("abc")
        self.driver.find_element(By.ID,"manager_name").send_keys("ttest")
        self.driver.find_element(By.ID,"register_tel").send_keys("1380000000")
        self.driver.find_element(By.ID,"submit_btn").click()
        return True

    def register_fail(self):
        self.driver.find_element(By.ID,"corp_name").send_keys("abc")
        self.driver.find_element(By.ID,"manager_name").send_keys("ttest")
        self.driver.find_element(By.ID,"register_tel").send_keys("1380000000")
        self.driver.find_element(By.ID,"submit_btn").click()
        return True



