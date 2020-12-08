import jsonpath
import requests

from Test_Demo_09day.demo2.base_api import BaseApi


class Tag(BaseApi):

    def __init__(self):
        corpsecret = 'QetRdrGubaqsGU_JqFXugMfbNLAxTAGY129ZS_vQQOc'
        super().__init__(secret=corpsecret)

    def find_group_id_by_name(self, group_name):
        print(self.get_list().json())
        for group in self.get_list().json()["tag_group"]:
            if group_name in group["group_name"]:
                return group["group_id"]
        print("group  name not in groups")
        return ""

    def is_group_id_exist(self, group_id):
        for group in self.get_list().json()["tag_group"]:
            if group_id in group["group_id"]:
                return True
        print("group id not in group")
        return False

    #
    # def get_token(self):
    #     corpid = 'wwfd249363e660c37a'
    #     corpsecret = 'QetRdrGubaqsGU_JqFXugMfbNLAxTAGY129ZS_vQQOc'
    #
    #     params = {"corpid": corpid,
    #               "corpsecret": corpsecret}
    #     res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
    #     access_token = jsonpath.jsonpath(res.json(), "$..access_token")[0]
    #     return access_token

    def get_list(self, tag_id=None):
        data = {"json": {"tag_id": tag_id},
                "url": f'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?access_token={self.token}',
                "method": "post"
                }

        res = self.send(data)
        print(res.json())
        return res

    def add_tag(self, tag_name, group_id=None, group_name=None, order=None):
        print(tag_name)
        data = {"json": {
            "group_id": group_id,
            "group_name": group_name,
            "order": order,
            "tag": tag_name},
            "url": f'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag?access_token={self.token}',
            "method": "post"

        }
        res = self.send(data)
        return res

    def add_and_detect(self, group_name, tag, **kwargs):
        r = self.add_tag(tag_name=tag, group_name=group_name, **kwargs)
        if r.json()["errcode"] == 40071:
            group_id = self.find_group_id_by_name(group_name)
            if not group_id:
                return ""
            self.delete_tag([group_id])
            self.add_tag(group_name=group_name, tag_name=tag)
        result = self.find_group_id_by_name(group_name=group_name)
        if not result:
            print("add not success")
        return result

    def delete_tag(self, tag_id=None, group_id=None):

        data = {"url": f'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag?access_token={self.token}',
                "json": {"tag_id": tag_id,
                         "group_id": group_id},
                "method": "post"}

        res = self.send(data)
        return res

    def delete_and_detect_group(self, group_ids):
        deleted_group_ids = []
        r = self.delete_tag(group_id=group_ids)
        if r.json()["errcode"] == 40068:
            # 如果标签不存在，就添加一个标签，将它的 group_id 存储进来
            for group_id in group_ids:
                if not self.is_group_id_exist(group_id):
                    group_id_tmp = self.add_and_detect(group_name="TMP00123",
                                                       tag=[{"name": "TAG1"}])
                    deleted_group_ids.append(group_id_tmp)
                # 如果标签存在，就将它存入标签组
                else:
                    deleted_group_ids.append(group_id)
            r = self.delete_tag(group_id=deleted_group_ids)
        return r
#
# if __name__ == "__main__":
#     token = Tag()
#     #     # token.get_token()
#     token.get_list()
#     token.add_tag(tag_name="test34ss23", group_id="etxAOwDwAAwC72OEYy0rVA-BA51sA0WQ")
