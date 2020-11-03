from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import TouchActions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestDelDemo2:
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": True

        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    def test_del(self):
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text = '通讯录']").click()
        search = self.driver.find_elements(MobileBy.XPATH,
                                  "//*[@class = 'android.widget.RelativeLayout' and @index = 0]/*[@class ='android.widget.TextView' and @clickable = 'true']")[0]
        search.click()
        ele = self.driver.find_element(MobileBy.XPATH,"//*[@text = '搜索']")
        ele.send_keys("lihao")
        # action = TouchActions(self.driver)
        # action.scroll_from_element(ele,0,10000).perform()
        result = self.driver.find_elements(MobileBy.XPATH,"//*[@class = 'android.widget.ListView']/*[@class = 'android.widget.RelativeLayout']")[-1]
        after_user_num = len(self.driver.find_elements(MobileBy.XPATH,"//*[@class = 'android.widget.ListView']/*[@class = 'android.widget.RelativeLayout']"))
        result.click()
        self.driver.find_element(MobileBy.XPATH,"//android.widget.RelativeLayout/*[@class = 'android.widget.TextView' and @clickable = 'true' and @long-clickable = 'false']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text = '编辑成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("删除成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text = '确定']").click()
        before_user_num = len(self.driver.find_elements(MobileBy.XPATH,"//*[@class = 'android.widget.ListView']/*[@class = 'android.widget.RelativeLayout']"))
        assert after_user_num-1 == before_user_num




