from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
import random
import time

class TestClassDemo():

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

    def test_addnumber(self):
        name = self.name()
        gread = "男"
        phone = self.random_phone()
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text = '通讯录']").click()
        # 通过滚动查找进行定位添加人员
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()
        # 点击手动添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text = '手动输入添加']").click()
        # 输入姓名
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@class = 'android.widget.RelativeLayout']/*[@text = '必填'] ").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()
        if gread == '男':
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element(MobileBy.XPATH,
                                                                          "//*[@text = '女']"))
            self.driver.find_element(MobileBy.XPATH,
                                     "//*[@text = '男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH,
                                     "//*[@text = '女']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text = '手机号']").send_keys(phone)
        self.driver.find_element(MobileBy.XPATH, "//*[@text = '保存']").click()
        # time.sleep(2)
        # print(self.driver.page_source)
        assert "添加成功" == self.driver.find_element(MobileBy.XPATH,"//*[@class = 'android.widget.Toast']").text

    def name(self):
        user = "lihao"
        name1 = random.randint(000000, 999999)
        return user + str(name1)

    def random_phone(self):
        phone = "138"
        n = random.randint(100000000, 999999999)
        phone += str(n)[1:]
        return phone
#
# if __name__ == "__main__":
#     TestClassDemo.test_addnumber("lihao", "13800000000", "男")
