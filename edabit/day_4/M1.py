"""Medium"""
"""https://edabit.com/challenge/2wQPKcSipXmK4idwD"""

#  items = {
#   "tv": 30,
#   "timmy": 20,
#   "stereo": 50,
# } ➞ "Timmy is gone..."
# # Timmy is in the dictionary.


#  items = {
#   "tv": 30,
#   "stereo": 50,
# } ➞ "Timmy is here!"
# # Timmy is not in the  dictionary.


# items = { } ➞ "Timmy is here!"
# # Timmy is not in the dictionary.

def find_it(items, name):

    if name in items.keys():
        return f"{name.capitalize()} is gone..."
    return f"{name.capitalize()} is here!"


items = {
  "tv": 30,
  "timmy": 20,
  "stereo": 50,
 }

print(find_it(items, 'timmy'))
