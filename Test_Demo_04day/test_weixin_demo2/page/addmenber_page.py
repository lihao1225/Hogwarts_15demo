from selenium.webdriver.common.by import By

from Test_Demo_04day.test_weixin_demo2.page.base_page import BasePage


class AddNumberPage(BasePage):
    # 姓名元素
    username_ele = (By.ID, "username")
    # 账号元素
    account_ele = (By.ID, "memberAdd_acctid")
    # 手机号元素
    phonenum_ele = (By.ID, "memberAdd_phone")
    # 保持按钮
    save_btn_ele = (By.CSS_SELECTOR, ".js_btn_save")
    # 同意勾选按钮
    checkbox_ele = (By.CSS_SELECTOR, ".ww_checkbox")
    # 用户信息
    user_ele = (By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')

    ele1 = (By.CSS_SELECTOR, ".ww_pageNav_info_text")

    ele2 = (By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal")

    def add_number(self, username, account, phonenum):
        self.find_ele(self.username_ele).send_keys(username)
        self.find_ele(self.account_ele).send_keys(account)
        self.find_ele(self.phonenum_ele).send_keys(phonenum)
        self.find_ele(self.save_btn_ele).click()
        self.wait_for_click(self.checkbox_ele)
        return True

    def get_number(self, value):

        # 验证联系人添加成功
        total_list = []
        while True:
            contactlist = self.find_eles(self.user_ele)
            titlelist = [element.get_attribute("title") for element in contactlist]
            total_list = total_list + titlelist
            print(titlelist)
            if value in titlelist:
                break
            result: str = self.find_ele(self.ele1).text
            num, total = result.split('/', 1)

            if int(num) == int(total):
                break
            else:
                self.find_ele(self.ele2).click()

        return total_list