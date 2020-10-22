import pytest


class TestLogin:


    def test_case1(self):
        print("case1")

    def test_case2(self, login, db):
        print("case2")

    def test_case3(self, login):
        print("case3")
