from Test_Demo_06day.test_weixin_demo3.page.app import App
from Test_Demo_06day.test_weixin_demo3.page.search_page import SearchPage
import pytest
import allure

class TestDel:

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        self.app.stop()

    @pytest.mark.run(order=2)
    def test_del_after(self):
        user_name = 'lihao'
        global num
        num = self.main.goto_address() \
        .goto_search() \
        .user(user_name)
        return num

    @pytest.mark.run(order=3)
    def test_del_num(self):
        user_name = 'lihao'
        del_success = self.main.goto_address() \
        .goto_search() \
        .search_user(user_name) \
        .goto_person_page() \
        .goto_edit_page() \
        .del_user()
        assert num == del_success+1


