# a = iter([1,2,3,4,5,6,7])

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

"""***********************************************************************"""

string = "hello anurodh how are you"
stir = iter(string)
print(next(stir))
print(next(stir))
print(next(stir))
print(next(stir))
print(next(stir))

l = [1,2,3,4,5]
itera = iter(l)
print(next(itera))
print(next(itera))
print(next(itera))
print(next(itera))
# print(next(itera))
# print(next(itera))

"""***********************************************************************"""

# class Iterator:

#     def __init__(self, n):
#         self.n = n
#         self.i = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.i < self.n:
#             self.i += 1
#             return self.i
#         else:
#             raise StopIteration


# it = Iterator(5)
# print(it)
# for i in it:
#     print(i)


"""***********************************************************************"""
