import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestHomework():

    def setup_method(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    # def teardown_method(self):
    #     # self.driver.quit()

    def test_homework(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # time.sleep(10)
        # cookies = self.driver.get_cookies()
        db = shelve.open("cookies")
        cookies = db["cookie"]
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.driver.find_element(By.XPATH, '//span[text()="导入通讯录"]').click()
        self.driver.find_element(By.XPATH, '//input[@class="ww_fileImporter_fileContainer_uploadInputMask"]').send_keys(
            r"D:\case_data.xlsx")
        file_name = self.driver.find_element(By.XPATH,
                                             '//div[@class="ww_fileImporter_fileContainer_fileNames"]').text
        assert file_name == "case_data.xlsx"
