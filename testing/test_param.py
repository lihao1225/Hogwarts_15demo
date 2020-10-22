import pytest


@pytest.mark.parametrize('b',[2, 3, 5])
@pytest.mark.parametrize('a', [1, 2, 4])
def test_param(a, b):
    print(a, b)
