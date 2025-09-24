# Append "fig" to the words list.

# Insert "blueberry" at index 1.

# Remove "date" from the list.

# Sort the list alphabetically.

# Reverse the list.

my_list='this is my list and i am using this on bluberry 7th date of the a month'.split()

# my_list.append('fig')
# print(my_list)

# my_list.insert(1,'blueberry')

# my_list.remove('date')

# my_list.sort()
# print(my_list)

# my_list.reverse()

# for x in my_list:
#     if len(x) >= 5:
#         print(x)

shortest = my_list[0]
longest= my_list[0]

for i in my_list:
    if len(shortest)> len(i):
        shortest=i

    if len(longest) < len(i):
        longest=i

print(f"Longest - {longest} and Shortest - {shortest}")