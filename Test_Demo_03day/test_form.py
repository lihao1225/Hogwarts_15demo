from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestForm:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element(By.ID,"user_login").send_keys("123")
        self.driver.find_element(By.ID,"user_password").send_keys("111")
        time.sleep(2)
        self.driver.find_element(By.ID,"user_remember_me").click()
        self.driver.find_element(By.XPATH,'//*[@id="new_user"]/div[4]/input').click()
        time.sleep(2)


