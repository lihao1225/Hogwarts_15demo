import selenium
from selenium import webdriver

class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(6)

    def teardown(self):
        self.driver.quit()


    def test_hogwarts(self):

        self.driver.get("https://ceshiren.com/")

