"""Hard"""

"""https://edabit.com/challenge/NYEaXXCnSj9jteNWA"""

# ave_spd(18, 20, 60) ➞ 30

# ave_spd(30, 10, 30) ➞ 15

# ave_spd(30, 8, 24) ➞ 12


def ave_spd(up_time, up_spd, down_spd):
    up_time_in_hr = up_time / 60
    distance = up_time_in_hr * up_spd
    down_time = distance / down_spd

    return (2 * distance) / (up_time_in_hr + down_time)


print(ave_spd(18, 20, 60))
print(ave_spd(30, 10, 30))
print(ave_spd(30, 8, 24))
