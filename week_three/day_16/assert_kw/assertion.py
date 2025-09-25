a = 10
b = 20
assert a + b != 30, "Wrong"
print("Assertion passed")

try:
    a = 10
    b = 20
    assert a + b != 30, "Wrong"
    print("Assertion passed")
except AssertionError as e:
    print(e)
