import re


def test_1():
    a = re.findall("([^:]+)$",'mobile existed:lihao29964582')
    print(a[0])
