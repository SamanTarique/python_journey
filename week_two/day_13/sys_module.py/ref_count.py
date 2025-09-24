import sys

a = 10
print(sys.getrefcount(a))
b = 10
print(sys.getrefcount(b))
