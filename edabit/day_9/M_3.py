"""Medium"""

"""https://edabit.com/challenge/5zDR5LyznNPsnEuYJ"""

import re


def Negation(my_string):
    return re.findall(r"[^a-zA-Z0-9\s]", my_string)


print(Negation(" alice15@gmail.com "))
print(Negation("anurodh kumar"))
print(Negation("+8988787656"))
print(Negation("!@#$%^&*()"))
