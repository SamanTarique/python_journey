"""Medium"""

"""https://edabit.com/challenge/2bTdN8sr3PQKkLHur"""


# divisible_by_b(17, 8) ➞ 24

# divisible_by_b(98, 3) ➞ 99

# divisible_by_b(14, 11) ➞ 22
# a will always be greater than b.


def divisible_by_b(a, b):
    return (b - a % b) + a


print(divisible_by_b(17, 8))
print(divisible_by_b(98, 3))
print(divisible_by_b(14, 11))
