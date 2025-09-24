# a = [1, 2, 3, 4, 5, 6, 7]
# b = (1, 2, 3, 4, 5)

# print(list(map(str, (a))))
# print(tuple(map(str, (b))))


# a = [1, 2, 3, 4, 5, 6, 7]


# def check_greater_5(x):
#     if x > 5:
#         return True
#     elif x < 5:
#         return False
#     else:
#         return "equal"


# x = map(check_greater_5, a)
# print(list(x))

# a = [1, 2, 3, 4, 5, 6, 7]
# print(list(map(lambda x: x ** 2, a)))
# print([i ** 2 for i in a])

a = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda c: (c * 9/5) + 32, a)))
print([(c * 9/5) + 32 for c in a])
