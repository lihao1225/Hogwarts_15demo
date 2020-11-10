from Test_Demo_07day.frame_demo.page.main_page import MainPage


class TestSearch:


    def test_search(self):


        main = MainPage().goto_market().goto_search().search()