a = 10
b = 5
c = 20
nums = input("enter 2 numbers")

"""Greatest of 3 numbers"""
# Logical AND
if (a > b) and (a > c):
    print(f"{a} is the largest number")
if (b > a) and (b > c):
    print(f"{b} uis the largest number")
if (c > a) and (c > b):
    print(f"{c} is the argest number")


# Logical OR
if (a < b) or (c > b):
    print(f"Either {a} < {b} OR {c} > {b} (or both)")

# Logical NOT
if not (a < b):
    print(f"{a} is not less than {b}")
