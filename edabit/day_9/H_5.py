"""Hard"""

"""https://edabit.com/challenge/zJSF5EfPe69e9sJAc"""

# censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"

# censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")

# censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"


def censor_string(my_string, my_list, replacer):
    for word in my_list:
        for 