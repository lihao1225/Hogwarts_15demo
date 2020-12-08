import random

import jsonpath
import pytest

from Test_Demo_09day.demo2.tag import Tag


class TestTag():

    def setup_class(self):
        self.tag = Tag()


    @pytest.mark.parametrize('tag_name,group_id',
                             (['test10', 'etxAOwDwAAnDxDV4csfHEhh9XUxUQRxA'],
                              ['1234', 'etxAOwDwAAnDxDV4csfHEhh9XUxUQRxA']
                              ))
    @pytest.mark.run(order=1)
    def test_add(self, tag_name, group_id):
        #随机生成标签名
        tag_name = tag_name + str(random.randint(00000, 999999))
        #根据标签组[etxAOwDwAAwC72OEYy0rVA-BA51sA0WQ]添加标签
        res = self.tag.add_tag(group_id=group_id, tag_name=[{"name":tag_name}])
        #根据返回结果获取tag_id
        tag_id = jsonpath.jsonpath(res.json(), "$..id")[0]
        #保存tag名
        # CaseData.tag_id = tag_id
        #根据tag_id查询返回结果
        name = self.tag.get_list(tag_id=tag_id)
        #使用jsonpath截取生成标签名
        n1 = jsonpath.jsonpath(name.json(), "$..name")[0]
        #断言接口返回code值
        assert res.status_code == 200
        #断言生成标签名和输入标签名
        assert tag_name == n1

    def test_add_tag(self):
        # todo: 测试数据要放到数据文件中
        group_name = "TMP00123"
        tag = [
            {"name": "TAG1"},
            {"name": "TAG2"},
            {"name": "TAG3"},
        ]

        r = self.tag.add_tag(group_name=group_name, tag_name=tag)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

    def test_add_and_detect(self):
        group_name = "TMP00123"
        tag = [
            {"name": "TAG1"},
            {"name": "TAG2"},
            {"name": "TAG3"},
        ]
        r = self.tag.add_and_detect(group_name=group_name, tag=tag)
        assert r

    def test_delete_and_detect_group(self):
        r = self.tag.delete_and_detect_group(["etxAOwDwAASbaSxWimBFnl7aXsvb1vLA"])
        assert r.json()["errcode"] == 0

    def test_get_list(self):
        self.tag.get_list()
