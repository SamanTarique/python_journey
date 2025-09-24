# def outer_function():
#     enclosing_var = "I am in the enclosing scope"

#     def inner_function():
#         nonlocal enclosing_var  # Modifies the enclosing_var
#         print(enclosing_var)
#         enclosing_var = "I was modified by inner"

#     inner_function()
#     print(enclosing_var)


# outer_function()

# print(["Even" if i % 2 == 0 else "odd" for i in range(1, 11)])

# li = [lambda arg=x: arg * 10 for x in range(1, 5)]
# for i in li:
#     print(i())
