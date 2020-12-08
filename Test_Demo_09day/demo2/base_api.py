import jsonpath
import requests


class BaseApi:

    def __init__(self,secret):
        self.token = self.get_token(secret=secret)

    def get_token(self,secret):
        corpid = 'wwfd249363e660c37a'

        params = {"corpid": corpid,
                  "corpsecret": secret}
        res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        access_token = jsonpath.jsonpath(res.json(), "$..access_token")[0]
        return access_token

    def send(self, data):
        r = requests.request(**data)
        return r
