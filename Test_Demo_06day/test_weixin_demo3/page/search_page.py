from appium.webdriver.common.mobileby import MobileBy

from Test_Demo_06day.test_weixin_demo3.page.base_page import BasePage
from Test_Demo_06day.test_weixin_demo3.page.personalinformationpage import PersonalInformationPage


class SearchPage(BasePage):
    # 搜索按钮元素
    search_ele = (MobileBy.XPATH, "//*[@text = '搜索']")

    # 搜索用户
    def search_user(self, user_name):
        self.find(*self.search_ele).send_keys(user_name)
        result = self.driver.find_elements(MobileBy.XPATH,
                                           "//*[@class = 'android.widget.ListView']/*[@class = 'android.widget.RelativeLayout']")
        last_user = result[-1]
        last_user.click()
        return PersonalInformationPage(self.driver)

    def user(self, user_name):
        self.find(*self.search_ele).send_keys(user_name)
        result1 = self.driver.find_elements(MobileBy.XPATH,"//*[@class = 'android.widget.ListView']/*[@class = 'android.widget.RelativeLayout']")
        after_user_num = len(result1)
        self.driver.back()
        self.driver.back()
        return after_user_num
