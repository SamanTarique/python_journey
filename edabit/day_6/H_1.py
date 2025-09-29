"""https://edabit.com/challenge/mHLAmj4vmRuXrT8Nb"""

# consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

# consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

# consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

# consecutive_combo([44, 46], [45]) ➞ True


def consecutive_combo(list1, list2):
    if abs(list1[len(list1) - 1] - list2[0]) == 1:
        return True
    return False


print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
print(consecutive_combo([44, 46], [45]))
