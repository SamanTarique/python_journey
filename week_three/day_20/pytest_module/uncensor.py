"""https://edabit.com/challenge/ehyZvt6AJF4rKFfXT"""

# uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

# uncensor("abcd", "") ➞ "abcd"

# uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"


def uncensor(my_string, vowel):
    new_string = my_string
    for i in vowel:
        new_string = new_string.replace("*", i, 1)

    return new_string


print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
