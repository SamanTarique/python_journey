"""Medium"""
"""https://edabit.com/challenge/5XXXppAdfcGaootD9"""

# sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# # 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

# sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])

# sum_odd_and_even([0, 0]) ➞ [0, 0])


def sum_odd_and_even(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    return [even, odd]


print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
print(sum_odd_and_even([0, 0]))
