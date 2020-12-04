import jsonpath
import requests


class Tag():

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'wwfd249363e660c37a'
        corpsecret = 'QetRdrGubaqsGU_JqFXugMfbNLAxTAGY129ZS_vQQOc'

        params = {"corpid": corpid,
                  "corpsecret": corpsecret}
        res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        access_token = jsonpath.jsonpath(res.json(), "$..access_token")[0]
        return access_token

    def get_list(self, tag_id=None):
        data = {"tag_id": tag_id}
        url = f'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?access_token={self.token}'
        res = requests.post(url=url, json=data)
        return res

    def add_tag(self, tag_name, group_id=None, group_name=None, order=None, tag_order=None):
        print(tag_name)
        data = {
            "group_id": group_id,
            "group_name": group_name,
            "order": order,
            "tag": [{
                "name": tag_name,
                "order": tag_order
            }
            ]
        }
        url = f'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag?access_token={self.token}'
        res = requests.post(url=url, json=data)

        return res

    def delete_tag(self, tag_id=None, group_id=None):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag?access_token={self.token}'
        data = {
            "tag_id": tag_id,
            "group_id": group_id
        }
        res = requests.post(url=url, json=data)
        return res

#
# if __name__ == "__main__":
#     token = Tag()
#     #     # token.get_token()
#     token.get_list()
#     token.add_tag(tag_name="test34ss23", group_id="etxAOwDwAAwC72OEYy0rVA-BA51sA0WQ")

