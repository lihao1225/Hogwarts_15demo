from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from Test_Demo_06day.test_weixin_demo3.page.base_page import BasePage


class ContactAddPage(BasePage):
    # 姓名元素
    name_ele = (MobileBy.XPATH, "//*[@class = 'android.widget.RelativeLayout']/*[@text = '必填'] ")
    # 性别元素
    sex_ele = (MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']")
    # 选项元素
    sex_weman_ele = (MobileBy.XPATH, "//*[@text = '女']")
    sex_man_ele = (MobileBy.XPATH, "//*[@text = '男']")
    # 手机号元素
    phone_ele = (MobileBy.XPATH, "//*[@text = '手机号']")
    # 保存按钮元素
    save_ele = (MobileBy.XPATH, "//*[@text = '保存']")

    def add_contact(self, name, gender, phone):
        # 输入姓名
        self.find(*self.name_ele).send_keys(name)
        # 点击性别
        self.find_and_click(*self.sex_ele)
        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*self.sex_weman_ele))
            self.find_and_click(*self.sex_man_ele)
        else:
            self.find_and_click(*self.sex_weman_ele)

        self.find(*self.phone_ele).send_keys(phone)
        self.find_and_click(*self.save_ele)
        # time.sleep(2)
        # print(self.driver.page_source)
        # assert "添加成功" == self.driver.find_element(MobileBy.XPATH, "//*[@class = 'android.widget.Toast']").text

        from Test_Demo_06day.test_weixin_demo3.page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)
