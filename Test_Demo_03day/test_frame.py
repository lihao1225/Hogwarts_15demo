from selenium.webdriver.common.by import By

from Test_Demo_03day.bast_method import BaseMethod
import time

class TestFrame(BaseMethod):

    def test_frame(self):

        self.driver.get("http://sahitest.com/demo/framesTest.htm")
        # frame_ele = self.driver.find_element(By.NAME,"top")
        self.driver.switch_to_frame(1)
        self.driver.find_element(By.XPATH,"//a[text()='Frames Test']").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.parent_frame()
        time.sleep(2)
