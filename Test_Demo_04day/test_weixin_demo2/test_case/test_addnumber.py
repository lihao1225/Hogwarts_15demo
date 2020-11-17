from Test_Demo_04day.test_weixin_demo2.page.main_page import MainPage
import random


class TestAddNumber():

    def setup(self):
        self.main = MainPage()
        self.main.user_cookies()
    def teardown(self):
        self.main.driver.quit()
    #通过通讯添加信息
    def test_add_number(self):
        username = self.username()
        account_num = self.account()
        phone_num = self.random_phone()
        add = self.main.goto_number().goto_addnumber()
        add.add_number(username=username, account=account_num, phonenum=phone_num)
        assert username in add.get_number(username)
    #通过首页添加信息
    # def test_add_number2(self):
    #     username = self.username()
    #     account_num = self.account()
    #     phone_num = self.random_phone()
    #     add = self.main.goto_addnumber()
    #     add.add_number(username=username, account=account_num, phonenum=phone_num)
    #     assert username in add.get_number(username)

    def username(self):
        user = "测试"
        name = str(random.randint(0000000, 99999999))
        user_name = user + name
        return user_name

    def account(self):
        account_num = random.randint(1000000, 999999999)
        return account_num

    def random_phone(self):
        phone = "138"
        n = random.randint(100000000, 999999999)
        phone += str(n)[1:]
        return phone
