# def even(li):
#     return li % 2 == 0


# res = filter(even, [1, 2, 3, 4, 5, 6])
# print(list(res))


# L = ["apple", "", None, "banana", 0, "cherry"]
# print(list(filter(None, L)))


L = ["apple", "", None, "banana", 0, "cherry"]
x = filter(lambda n: len(n) > 3, filter(None, L))
print(list(x))
