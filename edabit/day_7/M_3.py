"""https://edabit.com/challenge/QgSMSMpfcEebAyCye"""

# The parameter's format is as follows:
# (speed limit, avg speed, distance traveled at avg speed)

# time_saved(80, 90, 40) ➞ 3.3

# time_saved(80, 90, 4000) ➞ 333.3

# time_saved(80, 100, 40 ) ➞ 6.0

# time_saved(80, 100, 10) ➞ 1.5


def time_saved(speed_limit, avg_speed, dist_travelled):
    return (dist_travelled / speed_limit) * 60 - (dist_travelled / avg_speed) * 60


print(time_saved(80, 100, 10))
