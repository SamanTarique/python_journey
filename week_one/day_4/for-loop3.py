new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# for ele in range(10):
#     print(new_list[ele])

# for ele in range(0, 5):
#     print(new_list[ele])

# for ele in range(10, 0, -1):
#     print(new_list[ele])

# for ele in new_list:
#     if (ele % 2 == 0):
#         print("even")
#         continue
#     print("not even")
# else:
#     print("loop done")

# for ele in new_list:
#     if (ele == 5):
#         break
#     print(f"index - {ele}")

for ele in new_list:
    if ele < 7:
        print("Success")
    elif ele == 7:
        pass
    else:
        print("Failed")
