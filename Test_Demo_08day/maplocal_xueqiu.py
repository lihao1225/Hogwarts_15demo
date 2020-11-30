


from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    #修改判断条件
    if "quote.json" in flow.request.pretty_url:
        # 打开保存在本地的数据文件
        with open("/Users/huihuilina/Downloads/stock.json") as f:

            # 创建一个response
            flow.response = http.HTTPResponse.make(
                200,
                #读取文件内容作为数据
                f.read(),
                {"Content-Type": "application/json"}
            )