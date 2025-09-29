"""Medium"""
"""https://edabit.com/challenge/guR6aa2zytfZvywMS"""

# total_overs(2400) ➞ 400

# total_overs(164) ➞ 27.2
# # 27 overs and 2 balls were bowled by the bowler.

# total_overs(945) ➞ 157.3
# # 157 overs and 3 balls were bowled by the bowler.

# total_overs(5) ➞ 0.5


def total_overs(balls):
    if balls % 6 == 0:
        return balls//6
    elif balls < 6:
        return float("0." + str(balls))
    else:
        overs = balls // 6
        balls = balls % 6
        return float(f"{overs}.{balls}")


print(total_overs(2400))
print(total_overs(5))
print(total_overs(164))
print(total_overs(945))
