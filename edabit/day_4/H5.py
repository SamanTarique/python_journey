"""Hard"""
"""https://edabit.com/challenge/JzBLDzrcGCzDjkk5n"""

# a => 0
# e => 1
# i => 2
# o => 2
# u => 3


def encrypt(word):
    replace = {
        'a': 0,
        'e': 1,
        'i': 2,
        'o': 2,
        'u': 3
    }

    k = "".join([replace[i] if i in replace.keys() else i for i in reversed(word)])  

    print(k)
    # [replace[i] for i in reversed(word) replace[i] if i in replace.keys else i]


encrypt("hello")