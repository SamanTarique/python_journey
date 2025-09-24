my_list = list(map(int, input("inter elements of the list").split()))
print(my_list)

# for i in my_list[:]:
#     my_list.append(i ** 2)
#     print("here")
# print(my_list)

# *********************************************

new_list = []
for i in range(len(my_list)):
    print(type(i))
    if my_list[i] % 2 == 0:
        new_list.insert(i, 'Even')
    else:
        new_list.insert(i, 'Odd')
# print(new_list)


my_list.extend(new_list)
print(my_list)
