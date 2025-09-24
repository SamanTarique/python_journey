d = {1: "anurodh", 2: "kumar", 3: "python", "a": "hello", "b": "world"}

for key, value in d.items():
    print(f"key- {key} value- {value}")

i = 0
for key in d.keys():
    print(f"key[{i}]:{key}")
    i += 1

i = 0
for value in d.values():
    print(f"value at index {i} - {value}")
    i += 1
