from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://www.ceshiren.com")

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//li/a[text()="热门"]').click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//li/a[text()="所有分类"]')))
        self.driver.find_element(By.XPATH, '//li/a[text()="所有分类"]').click()
        ele = self.driver.find_element(By.XPATH, '//li/a[text()="所有分类"]')
        result = ele.get_attribute("class")
        print(result)
        # print(result)
        # assert result == "active"
