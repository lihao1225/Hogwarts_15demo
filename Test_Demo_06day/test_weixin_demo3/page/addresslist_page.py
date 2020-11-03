from appium.webdriver.common.mobileby import MobileBy

from Test_Demo_06day.test_weixin_demo3.page.base_page import BasePage
from Test_Demo_06day.test_weixin_demo3.page.member_invite_menu_page import MemberInviteMenuPage
from Test_Demo_06day.test_weixin_demo3.page.search_page import SearchPage


class AddressListPage(BasePage):
    search_ele = (MobileBy.XPATH,
                  "//*[@class = 'android.widget.RelativeLayout' and @index = 0]/*[@class ='android.widget.TextView' and @clickable = 'true']")

    def click_address(self):
        """

        :return:添加成员详情页
        """
        # 滑动查找【添加成员】
        self.find_by_scorll("添加成员").click()
        return MemberInviteMenuPage(self.driver)

    def goto_search(self):
        self.find_and_click(*self.search_ele)
        return SearchPage(self.driver)