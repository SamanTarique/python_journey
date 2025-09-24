# num = int(input("enter number-"))
num = input("enter number-")


# new_num = 0
# temp = num
# while (temp):
#     new_num = (new_num * 10) + (temp % 10)
#     temp //= 10

for i in range(len(num)//2):
    if num[i] != num[len(num) - i - 1]:
        print(False)
        exit()
print(True)

# print(f"{num == new_num}")
