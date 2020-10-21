import pytest
from Base_method.calculator import Calculator


@pytest.fixture(scope="module")
def prepare():
    cucal = Calculator()
    print("【计算开始】")
    yield cucal
    print("【计算结束】")
