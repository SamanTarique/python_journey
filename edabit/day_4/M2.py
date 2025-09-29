"""Medium"""
"""https://edabit.com/challenge/NNhkGocuPMcryW7GP"""


# square_areas_difference(5) ➞ 50

# square_areas_difference(6) ➞ 72

# square_areas_difference(7) ➞ 98

def square_areas_difference(num):
    square_side_len = (num**2 + num**2)**0.5  # pythagoras theorem
    return round((num*2) * (num*2) - (square_side_len*square_side_len))


print(square_areas_difference(5))
print(square_areas_difference(6))
print(square_areas_difference(7))
