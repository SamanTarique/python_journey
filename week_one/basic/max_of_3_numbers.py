try:
    nums = list(map(int, input("enter numbers").split()))
    print(nums)
    print(nums.sort())
    print(f"max- {nums[len(nums)-1]+ nums[len(nums)-2]}")
except Exception as e:
    print(f"error:{e}")

# a = [34, 23, 56, 7, 4, 2, 2, 4, 5, 34, 5, 7, 78, 75, 4, 33, 4]
# sm = -100000000
# for i in range(0, len(a)):
#     for j in range(i + 1, len(a)):
#         for k in range(j + 1, len(a)):
#             if sm < (a[i] + a[j] + a[k]):
#                 sm = a[i] + a[j] + a[k]
# print(sm)
