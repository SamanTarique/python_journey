"""M"""

"""https://edabit.com/challenge/BuCaGYh8keiWJGmcC"""


# Test.assert_equals(to_binary(0xFF), "11111111")
# Test.assert_equals(to_binary(0xAA), "10101010")
# Test.assert_equals(to_binary(0xFA), "11111010")


def to_binary(hex_string):
    return format(int(hex_string, 16), "b")


print(to_binary("0xFF"))
print(to_binary("0xAA"))
print(to_binary("0xFA"))
