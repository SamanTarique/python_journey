# d = {"name": "Prajjwal", 1: "Python", (1, 2): [1, 2, 4]}
# print(d['name'])
# print(d[(1, 2)])
# print(type(d[(1, 2)]))

d = {1: "anurodh", 2: "kumar", 3: "python", "a": "hello", "b": "world"}

del d[3]
print(d)

print(d.pop("u"))

print(d.popitem())
print(d)

print(d.clear())
print(d)

# d = {1: "1"}
# print(d.clear())
