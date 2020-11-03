from appium.webdriver.common.mobileby import MobileBy

from Test_Demo_06day.test_weixin_demo3.page.base_page import BasePage
from Test_Demo_06day.test_weixin_demo3.page.editpage import EditPage


class PersonalInformationTwoPage(BasePage):
    #编辑按钮
    edit_ele = (MobileBy.XPATH,"//*[@text = '编辑成员']")
    #进入编辑页
    def goto_edit_page(self):
        self.find_and_click(*self.edit_ele)
        return EditPage(self.driver)
