from mitmproxy import http


def request(flow: http.HTTPFlow):
    flow.request.headers["myheader"] = "lihao"
    print(flow.request.headers)
