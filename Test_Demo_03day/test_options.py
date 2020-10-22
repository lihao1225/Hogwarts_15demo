
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestOptions():


    def setup(self):
        options = Options()
        options.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://www.baidu.com")


