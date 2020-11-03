from appium.webdriver.common.mobileby import MobileBy

from Test_Demo_06day.test_weixin_demo3.page.base_page import BasePage


class EditPage(BasePage):
    #确认按钮
    confirm_ele = (MobileBy.XPATH,"//*[@text = '确定']")
    def del_user(self):
        self.find_by_scorll("删除成员").click()
        self.find_and_click(*self.confirm_ele)
        before_user_num = len(self.driver.find_elements(MobileBy.XPATH,
                                                        "//*[@class = 'android.widget.ListView']/*[@class = 'android.widget.RelativeLayout']"))
        return before_user_num