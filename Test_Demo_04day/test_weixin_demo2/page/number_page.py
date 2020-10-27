from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from Test_Demo_04day.test_weixin_demo2.page.addmenber_page import AddNumberPage
from Test_Demo_04day.test_weixin_demo2.page.base_page import BasePage

add_number_ele = (By.XPATH,"//div[@class ='js_has_member' ]/div[@class='ww_operationBar']/a[@class='qui_btn ww_btn js_add_member']")
class NumberPage(BasePage):

    def goto_addnumber(self):
        # add_ele = self.wait_for_click(add_number_ele)
        # add_ele.click()

        def wait_for_next(x: WebDriver):
            try:
                x.find_element(*add_number_ele).click()
                return x.find_element(By.ID,"username")
            except:
                return False
        WebDriverWait(self.driver,10).until(wait_for_next)
        return AddNumberPage(self.driver)
