from selenium.webdriver.common.by import By

from Test_Demo_03day.bast_method import BaseMethod
import time


class TestJS(BaseMethod):

    def test_js(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys("selenium测试")
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element(By.XPATH,"//*[@id='page']/div/a[10]").click()
        time.sleep(2)
