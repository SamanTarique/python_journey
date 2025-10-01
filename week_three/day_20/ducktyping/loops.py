def print_items(iterator):
    print(type(iterator))
    for item in iterator:
        print(item)


print_items([1, 2, 3])
print_items((10, 20, 30))
print_items({"a": 1, "b": 2})
print_items(x for x in range(3))
