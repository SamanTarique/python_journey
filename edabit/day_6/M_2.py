"""https://edabit.com/challenge/2RtztnzMDdyAj2MD3"""

# add("111", "111") ➞ "222"

# add("10", "80") ➞ "90"

# add("", "20") ➞ "Invalid Operation"

import re


def add(num_string1, num_string2):

    reg_exp = "^[\d]"
    if not re.match(reg_exp, num_string1) or not re.match(reg_exp, num_string1):
        return "Invalid Operation"

    return int(num_string1) + int(num_string2)


print(add("111", "111"))
print(add("10", "80"))
print(add("", "20"))
print(add("ascd", "20"))
