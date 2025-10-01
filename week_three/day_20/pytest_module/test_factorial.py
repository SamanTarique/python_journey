import math

import pytest
from factorial import factoraial


@pytest.fixture
def fact_fixture():
    int_list = [i for i in range(20)]
    return int_list


def test_fact(fact_fixture):
    for i in fact_fixture:
        assert factoraial(i) == math.factorial(i)
