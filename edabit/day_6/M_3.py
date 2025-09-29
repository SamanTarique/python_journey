"""https://edabit.com/challenge/BuwHwPvt92yw574zB"""

# list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]

# list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]


def list_of_multiples(num, length):
    return [i for i in range(num, (num * length) + 1, num)]


print(list_of_multiples(7, 5))
print(list_of_multiples(12, 10))
print(list_of_multiples(17, 6))
