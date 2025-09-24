# import os
# from math import pi, sqrt

# # import pandas as pd

# cwd = os.getcwd()
# print("Current working directory:", cwd)

# data = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# print(data)
# print(pi)
# print(sqrt(36))


# def isPrime(num):
#     if num < 2:
#         return False
#     count = 0
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             count = count + 1
#     if count > 0:
#         return False
#     return True

def isPrime(num: int):
    if num < 2:
        return False
    # count = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


print(isPrime('ss9'))
