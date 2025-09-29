# a, *b, c = (1, 2, 3, 4, 5)
# print(a, b, c)

# ****************************************************
# ls = [1, 2, 2, 3, 3, 0]
# print(ls.index(3))
# print(ls.count(2))
# print(all(ls))

# tup = 1, 2, 3, 4
# print(tup.index(3))
# print(tup.count(2))
# print(all(tup))

# print(tup)

# *****************************************************
# t = input("enter string")
# print((t))
# print((t,))
# print(tuple(t))
# print(list(t))

# **************************************
# a = list('anurodh')
# print(a)
# a = tuple('anurodh')
# print(a)

# **********************************************

# a = "anurodh"
# print(list(enumerate(list(a))))

# **********************************************

# a = [1, 2, 3, 4, 5, 6]
# b = (1, 2, 3, 4, 5, 6, 7)

# print(max(a))
# print(max(b))

# ************************************************

# a = [1, 2, 3, 4, 5, 6]
# b = (1, 2, 3, 4, 5, 6, 7)

# print(sum(a))
# print(sum(b))

# *************************************************

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = ["hello", "my", "name", "is", "anurodh", "kumar"]

# print(sorted(a, reverse=True))
# print(sorted(b, key=len))
# print(sorted(b, reverse=True, key=len))

# *****************************************************

# li = [4, 3, 567, 3, 43, 3]
# # t=(1,2,3)
# print(li.sort())
# print(sorted(li, reverse=True))
# print(li)


a = [(2, 4), (7, 9, 65), (4, 3, 5, 7, 8)]

print(sorted(a, key=lambda x: x[1]))
