"""Medium"""
"""https://edabit.com/challenge/5KqHNS9wS97zN7Xyy"""

# top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }

# top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }

# top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }


def top_note(student):

    res = dict({})

    res['name'] = student['name']
    res["top_note"] = max(student['notes'])
    return res


print(top_note({"name": "John", "notes": [3, 5, 4]}))
print(top_note({"name": "Max", "notes": [1, 4, 6]}))
print(top_note({"name": "Zygmund", "notes": [1, 2, 3]}))
