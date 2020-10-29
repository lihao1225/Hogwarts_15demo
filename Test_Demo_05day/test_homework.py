from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
import time


class TestHomeWork:

    def setup(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        # desired_caps["platformVersion"] = "6.0"
        desired_caps["deviceName"] = "127.0.0.1:7555"
        desired_caps["appPackage"] = "com.tencent.wework"
        desired_caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 跳过首页加载
        desired_caps["noReset"] = "True"
        # desired_caps["settings[waitForIdleTimeout]"] =0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)
        time.sleep(10)

    def teardown(self):
        self.driver.quit()



    def test_homework(self):
        # 定位工作台元素进行点击
        self.driver.find_element(MobileBy.XPATH, "//*[@text = '工作台']").click()
        # 通过滑动点击方法进行定位并且点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        # 通过update_settings方法设置动态加载时间
        self.driver.update_settings({"waitForIdleTimeout": 0})
        # 定位外出打卡并点击
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        # 定位打卡按钮并点击
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        # 断言判断
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
