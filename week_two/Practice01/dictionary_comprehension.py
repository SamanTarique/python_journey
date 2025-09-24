"""Mapping numbers to their squares
Create {1: 1, 2: 4, 3: 9, …, 10: 100}."""

# arr = [1, 2, 3, 4, 5, 6]
# d = {}
# print({key+1: value**2 for key, value in enumerate(arr)})

# print({i: i**2 for i in range(1, 11)})

"""Word count dictionary
Given "the quick brown fox jumps over the lazy dog",
count how many times each word appears."""

# string = input("enter string")
# print({word: string.count(word) for word in string.split()})

"""Filter dictionary
From { "a": 1, "b": 2, "c": 3, "d": 4 },
create a new dictionary with only even values."""
# d = {"a": 1, "b": 2, "c": 3, "d": 4}
# print({key: value for key, value in
#        {"a": 1, "b": 2, "c": 3, "d": 4}.items() if (
#             value % 2 == 0
#         )})

"""charcter count in a string"""
string = input("enter string ")
print({char: string.count(char)for char in "".join(string.split())})
print({char: string.count(char)for char in string})
