"""Hard"""

"""https://edabit.com/challenge/Xkc2iAjwCap2z9N5D"""

# has_friday_13(3, 2020) ➞ True

# has_friday_13(10, 2017) ➞ True

# has_friday_13(1, 1985) ➞ False

import datetime


def has_friday_13(month, year):
    return datetime.date(year, month, 13).weekday() == 4


print(has_friday_13(3, 2020))
print(has_friday_13(10, 2017))
print(has_friday_13(1, 1985))
