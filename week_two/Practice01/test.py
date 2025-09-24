my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# x = [lambda x=i: x[::-1] for i in my_list]
# for i in x:
#     print(i())

print([i[::-1] for i in my_list])
