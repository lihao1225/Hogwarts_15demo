from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys


class TestActions():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_action(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        dbl_click = self.driver.find_element(By.XPATH, "/html/body/form/input[2]")
        click = self.driver.find_element(By.XPATH, "//input[@value='click me']")
        right_click = self.driver.find_element(By.XPATH, "//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.double_click(dbl_click)
        action.click(click)
        action.context_click(right_click)
        action.perform()
        time.sleep(2)

    def test_moveto_element(self):
        self.driver.get("https://www.baidu.com")
        move_element = self.driver.find_element(By.XPATH, "//span[@id = 's-usersetting-top']")
        action = ActionChains(self.driver)
        action.move_to_element(move_element).perform()
        time.sleep(2)

    def test_drap_and_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element(By.ID, "dragger")
        drop_element = self.driver.find_element(By.XPATH, "//div[text()='Item 1']")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_element, drop_element).perform()

    def test_send_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element(By.XPATH, "/html/body/label[1]/input")
        action = ActionChains(self.driver)
        ele.click()
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1).perform()
        time.sleep(2)