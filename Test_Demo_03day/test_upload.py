from selenium.webdriver.common.by import By

from Test_Demo_03day.bast_method import BaseMethod


class TestUpload(BaseMethod):

    def test_upload(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.XPATH,"//span[@class = 'soutu-btn']").click()
        self.driver.find_element(By.XPATH,"//input[@class = 'upload-pic']").send_keys(r"D:\test.jpg")

