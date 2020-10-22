import pytest
import yaml


def get_data():
    with open(r"C:\Users\Administrator\PycharmProjects\Hogwarts_15demo\Test_demo_02day\cucal.yaml") as f:
        data = yaml.safe_load(f)
    return data["data"]


class TestDemo_02Day_Cucal:

    @pytest.mark.parametrize('a,b,c', get_data()["add"])
    @pytest.mark.run(order=1)
    def test_add(self, a, b, c, prepare):
        if type(a) == str or type(b) == str or type(c) == str:
            print("参数类型错误")
        else:
            result = prepare.add(a, b)
            try:
                assert result == c
            except AssertionError as e:
                print("输入参数错误请修改")
                print(e)
            else:
                print("{} + {} = {}".format(a, b, result))

    @pytest.mark.parametrize('a,b,c', get_data()["div"])
    @pytest.mark.run(order=-1)
    def test_div(self, a, b, c, prepare):
        if b == 0:
            print("除数不能为0")
        elif type(a) == str or type(b) == str or type(c) == str:
            print("参数类型错误")
        else:
            result = prepare.div(a, b)
            try:
                assert round(result, 1) \
                       == c
            except AssertionError as e:
                print("参数错误")
                print(e)
            else:
                print("{} / {} = {}".format(a, b, c))

    @pytest.mark.parametrize('a,b,c', get_data()["sub"])
    @pytest.mark.run(order=2)
    def test_sub(self, a, b, c, prepare):
        if type(a) == str or type(b) == str or type(c) == str:
            print("参数类型错误")
        else:
            result = prepare.sub(a, b)
            try:
                assert result == c
            except AssertionError as e:
                print("输入参数错误请修改")
                print(e)
            else:
                print("{} - {} = {}".format(a, b, result))

    @pytest.mark.parametrize('a,b,c', get_data()["mul"])
    @pytest.mark.run(order=3)
    def test_mul(self, a, b, c, prepare):
        result = prepare.mul(a, b)
        try:
            assert result == c
        except AssertionError as e:
            print("输入参数错误请修改")
            print(e)
        else:
            print("{} * {} = {}".format(a, b, result))
