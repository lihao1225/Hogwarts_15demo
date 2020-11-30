from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "https://www.baidu.com/":
        # 发起请求，判断URL是不是我们预期的URL
        flow.response = http.HTTPResponse.make(
            # 创建一个response
            200,
            b"hello world",
            {"Content-Type": "text/html"}
        )
