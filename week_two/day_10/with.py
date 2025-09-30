# a = 'anurodh'
# with open("with.txt", "w") as file:
#     print(file.write(a))

# with open('with.txt', 'r') as file:
#     print(file.read())

with open("/home/developer/projects/python/with.txt", "r+") as file:
    print(file.read())
    print(file.readline())
    print(file.readlines())
    print(file.readable())
