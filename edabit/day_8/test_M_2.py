import pytest
from M_2 import fix_import


@pytest.mark.parametrize(
    "import_string, result",
    [
        ("import randint from random", "from random import randint"),
        ("import pi from math", "from math import pi"),
        ("import object from module_name", "from module_name import object"),
    ],
)
def test_fix_import(import_string, result):
    assert fix_import(import_string) == result
