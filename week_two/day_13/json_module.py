import json

a = {"name": "anurodh", "age": 22, "role": "software developer"}

print(a, type(a))
json_obj = json.dumps(a, indent=4)
print(json_obj, type(json_obj))


decoded_dict = json.loads(json_obj)
print("\nDecoded Python Dictionary:")
print(decoded_dict, type(decoded_dict))
