"""Medium"""

"""https://edabit.com/challenge/Cjtm4CpLzHDerQMfX"""

# area_of_country("Russia", 17098242) ➞ "Russia is 11.48% of the total world's landmass"

# area_of_country("USA", 9372610), "USA is 6.29% of the total world's landmass"

# area_of_country("Iran", 1648195) ➞ "Iran is 1.11% of the total world's landmass"

world_area = 148940000


def area_of_country(name, area):
    country_area = area / world_area * 100
    return f"{name} is {country_area:.2f}% of the total world's landmass"


print(area_of_country("Russia", 17098242))
print(area_of_country("USA", 9372610))
print(area_of_country("Iran", 1648195))
