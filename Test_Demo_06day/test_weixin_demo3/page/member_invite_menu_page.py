from appium.webdriver.common.mobileby import MobileBy

from Test_Demo_06day.test_weixin_demo3.page.base_page import BasePage


class MemberInviteMenuPage(BasePage):
    add_ele = (MobileBy.XPATH, "//*[@text = '手动输入添加']")

    def add_member_menual(self):
        # 点击手动添加
        self.find_and_click(*self.add_ele)
        # 局部调用
        from Test_Demo_06day.test_weixin_demo3.page.contactadd_page import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        result = self.get_toast_text()
        self.driver.back()


        return result
