"""Hard"""

"""https://edabit.com/challenge/ksiA6Q34iXgTcMeZF"""

# Days	Bonus
# 0 to 32 days	Zero
# 33 to 40 days	SGD$325 per billable day
# 41 to 48 days	SGD$550 per billable day
# Greater than 48 days	SGD$600 per billable day

# bonus(15) ➞ 0

# bonus(37) ➞ 1625

# bonus(50) ➞ 8200


def bonus(days):
    my_dict = {"0 32": 0, "33 40": 325, "41 48": 550, "49 999999999": 600}
    payment = 0

    if days <= 32:
        return 0

    for day_range, wage in my_dict.items():
        start_day, end_day = map(int, day_range.split())
        if start_day > days:
            break

        if end_day < days:
            day_diff = (end_day - start_day) + 1
        else:
            day_diff = (days - start_day) + 1

        payment += wage * day_diff
    return payment


print(bonus(15))
print(bonus(37))
print(bonus(50))
