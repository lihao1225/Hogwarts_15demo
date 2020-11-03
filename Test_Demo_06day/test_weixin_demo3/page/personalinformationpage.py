from appium.webdriver.common.mobileby import MobileBy

from Test_Demo_06day.test_weixin_demo3.page.base_page import BasePage
from Test_Demo_06day.test_weixin_demo3.page.personalinformationtwopage import PersonalInformationTwoPage


class PersonalInformationPage(BasePage):

    person_page_ele = (MobileBy.XPATH,
                                 "//android.widget.RelativeLayout/*[@class = 'android.widget.TextView' and @clickable = 'true' and @long-clickable = 'false']")

    #进入个人页面第二层
    def goto_person_page(self):
        self.find_and_click(*self.person_page_ele)
        return PersonalInformationTwoPage(self.driver)

