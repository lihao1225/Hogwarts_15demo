import random

from Test_Demo_09day.demo2.address import Address


class TestAddress():

    def setup(self):
        self.address = Address()

    def test_add(self):
        name = self.name()
        userid = self.user_id()
        mobile = self.mobile()
        self.address.add_num(name=name, userid=userid, mobile='13810752512', department=[2])
        res = self.address.get_num(userid=userid)
        assert res.json()["userid"] == userid
        assert res.json()["errcode"] == 0

    def test_department(self):
        self.address.get_partyid()

    def test_add_and_delete(self):
        name = self.name()
        userid = self.user_id()
        mobile = self.mobile()
        self.address.add_and_delete(name=name, userid=userid, mobile=mobile, department=[])

    def test_get_user(self):
        res = self.address.get_num(userid="123457")
        assert res.json()['errcode'] == 0
        assert res.json()['userid'] == 'LiHao'

    def test_delete(self):
        res = self.address.delete(userid='lihao')
        print(res.json())

    def test_delete_and_add(self):
        res = self.address.delete_and_add(userid='lihao')
        print(res)

    def test_update(self):
        res = self.address.update(userid="lihao")
        print(res.json())

    def name(self):
        str1 = "测试"
        str2 = str(random.randint(000000, 999999))
        name = str1 + str2
        return name

    def user_id(self):
        user = "lihao"
        ids = str(random.randint(1000000, 99999999))
        userid = user + ids
        return userid

    def mobile(self):
        phone = "138"
        num = str(random.randint(100000000, 999999999))
        mobile = phone + num[1:]
        return mobile
