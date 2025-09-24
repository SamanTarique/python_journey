"""Table of a number"""

# n = int(input("enter number"))
# squares = [n * i for i in range(1, 11)]
# print(squares)

"""Squares of a number"""

# my_list = [i**2 for i in range(1, 101)]
# print(my_list)

"""Even numbers only"""

# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 23.56, 48, 64, 67, 58, 60, 24]

# print([i for i in my_list if i % 2 == 0])

"""Even numbers only in range (1,100)"""

# print([i for i in range(1, 101) if i % 2 == 0])

"""Find all numbers from 1 to 100 that are divisible by both 3 and 5"""

# print([i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0])

"""Given [[1, 2], [3, 4], [5, 6]], flatten it into [1, 2, 3, 4, 5, 6]"""

# nested_array = [[1, 2], [3, 4], [5, 6]]
# print([element for array in nested_array for element in array])

# nested_array = [[1, 2, [3, 4]], [5, [6, 7, [8]]], 9]


# def nested(nested_array):
#     return [item for sub_list in nested_array for item in (
#         nested(sub_list) if isinstance(sub_list, list) else [sub_list]
#         )]


# print(nested(nested_array))


"""From a string, extract all vowels into a list."""
# string = input("enter string")
# print([i for i in string if (
#     i == 'a' or i == 'i' or i == 'e' or i == 'o' or i == 'u'
#     )])

# vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
# print([i for i in string if i in vowels])
