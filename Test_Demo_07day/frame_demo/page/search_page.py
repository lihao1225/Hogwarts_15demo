import os

from selenium.webdriver.common.by import By

from Test_Demo_07day.frame_demo.common.handle_path import DataDir
from Test_Demo_07day.frame_demo.page.base_page import BasePage


class SearchPage(BasePage):

    def search(self):
        # self.find(By.XPATH,'//*[@resource-id = "com.xueqiu.android:id/search_input_text"]').send_keys("alibaba")
        file_name = os.path.join(DataDir,"search.yaml")
        self.parse_yaml(file_name,"search")
