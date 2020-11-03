import random
import pytest
from Test_Demo_06day.test_weixin_demo3.page.app import App


class TestAdd:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.run(order=1)
    def test_add_num(self):
        name = self.name()
        gender = "男"
        phone = self.random_phone()

        result = self.main.goto_address() \
            .click_address(). \
            add_member_menual(). \
            add_contact(name, gender, phone) \
            .get_toast()
        print(result)
        assert '添加成功' == result

    def name(self):
        user = "lihao"
        name1 = random.randint(000000, 999999)
        return user + str(name1)

    def random_phone(self):
        phone = "138"
        n = random.randint(100000000, 999999999)
        phone += str(n)[1:]
        return phone
