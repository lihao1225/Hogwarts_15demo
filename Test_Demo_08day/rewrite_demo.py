import json
from mitmproxy import http


def response(flow:http.HTTPFlow):
    #加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        #把相应数据转化为python对象，保存到data中
        data = json.loads(flow.response.content)
        #修改第一支股票的名称
        name = data['data']['items'][1]['quote']['name']
        data['data']['items'][1]['quote']['name'] = name*2
        data['data']['items'][2]['quote']['name'] = ''
        #把修改后的内容赋值给respons原始数据
        flow.response.text = json.dumps(data)
