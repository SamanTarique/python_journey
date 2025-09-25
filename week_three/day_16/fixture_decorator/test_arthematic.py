import pytest
from arthematic import add


@pytest.fixture
def input_data():
    a, b = map(int, input("Enter 2 numbers- ").split())
    print(a, b, type(a))
    return a, b


def test_add(input_data):
    assert add(input_data[0], input_data[1]) == input_data[0] + input_data[1]
