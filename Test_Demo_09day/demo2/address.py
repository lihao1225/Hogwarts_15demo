import random
import re

import jsonpath

from Test_Demo_09day.demo2.base_api import BaseApi


class Address(BaseApi):

    def __init__(self):
        sec = 'Hlj6iwDxSZCr-bT3ok_GnA3MzIpeQqIjAXeIEa0R02M'
        super().__init__(secret=sec)

    # 添加用户信息
    def add_num(self, userid, name, **kwargs):
        data = {"url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
                "json": {"userid": userid, "name": name, **kwargs},
                "method": "post"
                }
        res = self.send(data)
        print(res.json())
        return res

    def add_and_delete(self, userid, name, **kwargs):
        res = self.add_num(userid, name, **kwargs)
        errcode = res.json()['errcode']
        # userid出现相同的时候
        if errcode == 60102:
            user_id = self.get_num(userid).json()['userid']
            if not user_id:
                return ""
            self.delete(userid)
            self.add_num(userid, name, **kwargs)
            result = self.get_num(userid).json()['userid']
            if not result:
                print("add not success")
            return result
        # 当出现手机号相同情况
        elif errcode == 60104:
            # 根据错误信息返回拿到user_id
            msg = res.json()['errmsg']
            user = re.findall("([^:]+)$", msg)[0]
            # 判断是否存在手机号
            mobile = self.get_num(user).json()['mobile']
            if not mobile:
                return ""
            self.delete(user)
            self.add_num(userid, name, **kwargs)
            result = self.get_num(userid).json()['userid']
            if not result:
                print("add not success")
            return result
        # 手机号和邮箱为空的情况
        elif errcode == 60129:
            phone = "138"
            num = str(random.randint(100000000, 999999999))
            mobile = phone + num[1:]
            email = mobile + "@gzdev.com"
            self.add_num(userid, name, email=email, **kwargs)
        # 当部门为空或者不存在时候
        elif errcode == 40066:
            print("不合法的部门列表")

    # 获取成员信息
    def get_num(self, userid):
        data = {"url": f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}",
                "method": "get"
                }
        res = self.send(data)
        print(res.json())
        return res

    def update(self, userid, **kwargs):
        data = {
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
            "json": {"userid": userid, **kwargs},
            "method": "post"
        }
        res = self.send(data)
        return res

    # 删除接口
    def delete(self, userid):
        data = {"url": f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}",
                "method": "get"
                }
        res = self.send(data)
        return res

    def delete_and_add(self, userid):
        res = self.delete(userid)
        errcode = res.json()["errcode"]
        # userid不存在
        if errcode == 60111:
            user = self.get_num(userid).json()["errmsg"]
            if 'userid not found' != user:
                return ""
            self.add_num(userid=userid, name="99999", monile=1388888888, department=[2])
            result = self.delete(userid)
            if result.json()["errcode"] != 0:
                print("delete fail")
            return result
        elif errcode == 301005:
            print("不允许删除创建者")

    def get_partyid(self, par_id=None):
        # par_id 为空时，获取所有部门信息
        data = {"method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
                "params": {"access_token": self.token, "id": par_id}}
        res = self.send(data)
        return res
