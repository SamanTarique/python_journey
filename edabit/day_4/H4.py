"""Hard"""
"""https://edabit.com/challenge/st8mDxreMcuWxuz8c"""


def pentagonal(num):
    if num == 1:
        return 1

    return (num-1)*5 + pentagonal(num-1)


print(pentagonal(3))
print(pentagonal(4))
print(pentagonal(5))
print(pentagonal(6))
print(pentagonal(7))
print(pentagonal(8))
