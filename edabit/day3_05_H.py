"""Hard"""
"""https://edabit.com/challenge/yvJbdkmKHvCNtcZy9"""
# is_disarium(75) ➞ False
# # 7^1 + 5^2 = 7 + 25 = 32

# is_disarium(135) ➞ True
# # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

# is_disarium(544) ➞ False

# is_disarium(518) ➞ True

# is_disarium(466) ➞ False

# is_disarium(8) ➞ True


def is_disarium(n):
    sum = 0
    orignal = n

    for index, num in enumerate(str(n), start=1):
        sum += int(num)**int(index)
        # sum += math.pow(num, index)

    if orignal == sum:
        return True
    return False


print(is_disarium(200))
print(is_disarium(125))
print(is_disarium(135))
print(is_disarium(75))
print(is_disarium(544))
print(is_disarium(518))
print(is_disarium(466))
print(is_disarium(8))
