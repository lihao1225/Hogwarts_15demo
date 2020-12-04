import random
import jsonpath
import pytest
from Test_Demo_09day.datas import CaseData
from Test_Demo_09day.tag import Tag


class TestTag():

    def setup(self):
        self.tag = Tag()

    @pytest.mark.parametrize('tag_name,group_id',
                             (['test10', 'etxAOwDwAAwC72OEYy0rVA-BA51sA0WQ'],
                              ['1234', 'etxAOwDwAAwC72OEYy0rVA-BA51sA0WQ']
                              ))
    @pytest.mark.run(order=1)
    def test_add(self, tag_name, group_id):
        #随机生成标签名
        tag_name = tag_name + str(random.randint(00000, 999999))
        #根据标签组[etxAOwDwAAwC72OEYy0rVA-BA51sA0WQ]添加标签
        res = self.tag.add_tag(group_id=group_id, tag_name=tag_name)
        #根据返回结果获取tag_id
        tag_id = jsonpath.jsonpath(res.json(), "$..id")[0]
        #保存tag名
        CaseData.tag_id = tag_id
        #根据tag_id查询返回结果
        name = self.tag.get_list(tag_id=tag_id)
        #使用jsonpath截取生成标签名
        n1 = jsonpath.jsonpath(name.json(), "$..name")[0]
        #断言接口返回code值
        assert res.status_code == 200
        #断言生成标签名和输入标签名
        assert tag_name == n1

    def teardown(self):
        #调用保存的tag_id
        tag_id = getattr(CaseData, "tag_id")
        #根据tag_id调用删除接口
        self.tag.delete_tag(tag_id=tag_id)
        #调用获取列表接口
        res = self.tag.get_list()
        # for tag_ids in res.json()['tag_group']:
        #     if tag_ids['group_id'] == 'etxAOwDwAAwC72OEYy0rVA-BA51sA0WQ':
        #         for ids in tag_ids["tag"]:
        #             print(ids['id']
        #列表推到式获取标签组为[etxAOwDwAAwC72OEYy0rVA-BA51sA0WQ]中所有tag_id
        id_list = [ids['id'] for tag_ids in res.json()['tag_group'] if
                   tag_ids['group_id'] == 'etxAOwDwAAwC72OEYy0rVA-BA51sA0WQ'
                   for ids in tag_ids["tag"]]
        #断言删除tag_id是否在以有组里
        assert tag_id not in id_list
