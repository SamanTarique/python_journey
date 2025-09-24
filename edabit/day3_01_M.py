"""Medium"""
"""https://edabit.com/challenge/3Ekam9jvbNKHDtx4K"""
# line_length([15, 7], [22, 11]) ➞ 8.06

# line_length([0, 0], [0, 0]) ➞ 0

# line_length([0, 0], [1, 1]) ➞ 1.41

import math


def line_length(dot1, dot2):
    return f"{math.sqrt((dot2[0] - dot1[0])**2 + (dot2[1] - dot1[1])**2):.2f}"


print(line_length([15, 7], [22, 11]))
print(line_length([0, 0], [0, 0]))
print(line_length([0, 0], [1, 1]))
