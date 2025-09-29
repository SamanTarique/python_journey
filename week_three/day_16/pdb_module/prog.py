# import pdb

# pdb.set_trace()
name1 = input("Enter name")
name2 = input("Enter name")
# breakpoint()
sum = 0
for i in range(1, 7):
    for j in range(1, 4):
        sum += i + j
        print(sum, i, j)

print("sum=", sum)
