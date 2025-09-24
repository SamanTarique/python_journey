# try:
#     s = str(input("enter a string"))

#     if len(s) == 1:
#         exit()

#     s = list(s)
#     left = 0
#     right = len(s) - 1

#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1

#     print("".join(s))
# except Exception as e:
#     print(f"Some Error occured: {e}")

# ***************************************************

# print(''.join(reversed(input("enter string"))))

# ****************************************************

# rev = 'hello'[::-1]
# print(rev)

# ******************************************************
# string = input("enter the string")
# print(''.join(string[i] for i in range(len(string)-1, -1, -1)))
