from selenium.webdriver.common.by import By

from Test_Demo_03day.bast_method import BaseMethod


class TestWindow(BaseMethod):

    def test_windows(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.XPATH, "//div[@id = 'u1']/a[@name = 'tj_login']").click()
        self.driver.find_element(By.XPATH, "//a[text()='立即注册']").click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element(By.XPATH, "//input[@id = 'TANGRAM__PSP_4__userName']")
