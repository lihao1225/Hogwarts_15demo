import shelve

from selenium.webdriver.common.by import By

from Test_Demo_04day.test_weixin_demo2.page.addmenber_page import AddNumberPage
from Test_Demo_04day.test_weixin_demo2.page.base_page import BasePage
import time

from Test_Demo_04day.test_weixin_demo2.page.number_page import NumberPage

class MainPage(BasePage):
    # 通讯录元素
    number_ele = (By.XPATH, "//a[@id ='menu_contacts' ]/span[@class='frame_nav_item_title']")
    #添加成员按钮
    add_number_ele = (By.XPATH, "//div/span[@class = 'ww_indexImg ww_indexImg_AddMember']")
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # def get_cookie(self):
    #
    #     time.sleep(15)
    #     cookies = self.driver.get_cookies()
    #     db = shelve.open("cookies")
    #     db["cookie"] = cookies
    #     db.close()
    def user_cookies(self):
        db = shelve.open("cookies")
        cookies = db["cookie"]
        db.close()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        # time.sleep(10)


    def goto_number(self):
        self.find_ele(locator=self.number_ele).click()
        return NumberPage(self.driver)


    def goto_addnumber(self):
        self.find_ele(self.add_number_ele).click()
        return AddNumberPage(self.driver)
# if '__main__' == __name__:
#     # MainPage().user_cookies()
#     MainPage().get_cookie()
