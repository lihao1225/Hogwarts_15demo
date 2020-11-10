import os

from selenium.webdriver.common.by import By

from Test_Demo_07day.frame_demo.common.handle_path import DataDir
from Test_Demo_07day.frame_demo.page.base_page import BasePage
from Test_Demo_07day.frame_demo.page.search_page import SearchPage


class MarketPage(BasePage):

    def goto_search(self):
        file_name = os.path.join(DataDir,"market.yaml")
        self.parse_yaml(file_name,"goto_search")
        # self.find(By.XPATH, "//*[@resource-id = 'com.xueqiu.android:id/action_search']").click()
        return SearchPage(self.driver)