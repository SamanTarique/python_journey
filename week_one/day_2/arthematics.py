# + - * / ** %

def arth(a, b, operation):
    if operation == 'sum':
        return a + b
    elif operation == 'sub':
        return a - b
    elif operation == 'mul':
        return a * b
    elif operation == 'div':
        return a / b
    elif operation == 'mod':
        return a % b
    elif operation == 'pow':
        return a ** b
    else:
        print("Invalid Operation")


try:
    nums_input = input("enter 2 numbers")
    nums = list(map(float, nums_input.split()))

    if len(nums) != 2:
        print('need 2 numbers')
    print(arth(nums[0], nums[1], 'mul'))
except ValueError:
    print("Error: Please enter valid numeric values (e.g., 7.5 9.3).")
