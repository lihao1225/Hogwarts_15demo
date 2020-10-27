from Test_Demo_04day.test_weixin_demo.page.index_page import IndexPage


class TestRegisterWX():

    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        assert self.index.goto_register().register_successful()
