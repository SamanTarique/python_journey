"""https://edabit.com/challenge/co4nwXSvnCjGEu8vp"""

# format_date("11/12/2019") ➞ "20191211"

# format_date("12/31/2019") ➞ "20193112"

# format_date("01/15/2019") ➞ "20191501"


def format_date(date_string):
    return "".join(reversed(date_string.split("/")))


print(format_date("11/12/2019"))
print(format_date("12/31/2019"))
print(format_date("01/15/2019"))
