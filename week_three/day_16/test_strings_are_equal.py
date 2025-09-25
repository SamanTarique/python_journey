from pytest_framework.equal_string import strings_are_equal


def test_strings_are_equal():
    assert strings_are_equal("hello", "hello") == "hello == hello"
    assert strings_are_equal("test", "test") == "test == test"
