"""Inmplicit type conversion"""

integer_num = 10
float_num = 12.6
result = integer_num * float_num

print(f"type {type(integer_num)} type {type(float_num)} type {type(result)}")
print(f"Implicit type conversion {result}")

age = 24
print(f"My age is {age}")
print(type(f"My age is {age}"))


"""Explicit type conversion"""
string = int(input())
print(string)
