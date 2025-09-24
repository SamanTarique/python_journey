# num_list = list(map(int, input("enter 2 nums").split()))
num1, num2 = map(int, input("enter 2 nums").split())

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"num1 - {num1} num2 - {num2}")
