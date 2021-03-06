"""
app.py 模块，存放app相关的一些操作。
比如 启动应用，重启应用，停止应用，进入到首页
"""
import yaml
from appium import webdriver

from Test_Demo_06day.test_weixin_demo3.page.base_page import BasePage
from Test_Demo_06day.test_weixin_demo3.page.main_page import MainPage

with open(r'C:\Users\Administrator\PycharmProjects\Hogwarts_15demo\Test_Demo_06day\test_weixin_demo3\datas\caps.yaml') as f:
    myconfig = yaml.safe_load(f)
    caps = myconfig['desirecaps']
    ip = myconfig['server']['ip']
    port = myconfig['server']['port']


class App(BasePage):
    def start(self):
        if self.driver == None:
            # 启动app
            # 定义了一个字典
            # caps = {}
            # caps["platformName"] = "Android"
            # caps["deviceName"] = "hogwarts"
            # caps["appPackage"] = "com.tencent.wework"
            # caps["appActivity"] = ".launch.LaunchSplashActivity"
            # # noReset 保留缓存， 比如登录状态
            # caps["noReset"] = "True"
            # # 不停止应用，直接运行测试用例
            # caps["dontStopAppOnReset"] = "true"
            # caps['skipDeviceInitialization'] = 'true'
            # caps['skipServerInstallation'] = 'true'
            # # caps["settings[waitForIdleTimeout]"] = 0
            # # 关键  localhost:4723  本机ip:server端口
            # desired_caps = {
            #     "platformName": "android",
            #     "deviceName": "127.0.0.1:7555",
            #     "appPackage": "com.tencent.wework",
            #     "appActivity": ".launch.LaunchSplashActivity",
            #     "noReset": True
            #
            # }
            # self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
            #
            # self.driver.implicitly_wait(30)

            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", caps)
            self.driver.implicitly_wait(15)
        else:
            self.driver.launch_app()
            # self.driver.start_activity(package,activity)

        return self

    def restart(self):
        # 重启 app
        self.driver.close_app()
        self.driver.launch_app()
        pass

    def stop(self):
        # 停止 app
        self.driver.quit()

    def goto_main(self) -> MainPage:
        # 进入到首页
        return MainPage(self.driver)