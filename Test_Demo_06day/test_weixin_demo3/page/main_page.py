from appium.webdriver.common.mobileby import MobileBy

from Test_Demo_06day.test_weixin_demo3.page.addresslist_page import AddressListPage
from Test_Demo_06day.test_weixin_demo3.page.base_page import BasePage

# 主页面
from Test_Demo_06day.test_weixin_demo3.page.search_page import SearchPage


class MainPage(BasePage):


    #通讯录元素
    tel_ele = (MobileBy.XPATH, "//*[@text = '通讯录']")


    def goto_message(self):
        """

        :return:
        """
        pass

    def goto_address(self):
        """

        :return:通讯的列表页
        """
        self.find_and_click(*self.tel_ele)
        return AddressListPage(self.driver)

