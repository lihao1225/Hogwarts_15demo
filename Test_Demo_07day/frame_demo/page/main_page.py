import os

from selenium.webdriver.common.by import By

from Test_Demo_07day.frame_demo.common.handle_path import DataDir
from Test_Demo_07day.frame_demo.page.base_page import BasePage
from Test_Demo_07day.frame_demo.page.mark_page import MarketPage


class MainPage(BasePage):

    def goto_market(self):
        # self.find(By.XPATH, "//*[@resource-id = 'com.xueqiu.android:id/post_status']").click()
        # self.find(By.XPATH, "//*[@resource-id = 'android:id/tabs']//*[@text = '行情']").click()
        file_name = os.path.join(DataDir, "main.yaml")
        self.parse_yaml(file_name, "goto_market")

        return MarketPage(self.driver)
