"""Medium"""

"""https://edabit.com/challenge/Axim3Ld5zu9RFLZKr"""

# invert({ "z": "q", "w": "f" })
# ➞ { "q": "z", "f": "w" }

# invert({ "a": 1, "b": 2, "c": 3 })
# ➞ { 1: "a", 2: "b", 3: "c" }

# invert({ "zebra": "koala", "horse": "camel" })
# ➞ { "koala": "zebra", "camel": "horse" }


def invert(my_dict):
    my_list = []
    for item in my_dict.items():
        my_list.append(reversed(item))

    return dict(my_list)


print(invert({"z": "q", "w": "f"}))
print(invert({"a": 1, "b": 2, "c": 3}))
print(invert({"zebra": "koala", "horse": "camel"}))
