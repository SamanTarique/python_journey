def arthematic_operation(operand1, operator, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '//' or operator == '/':
        if operand2 <= 0:
            return -1
        elif operator == '//':
            return operand1 // operand2
        else:
            return operand1 / operand2
    elif operator == '%':
        return operand1 % operand2
    else:
        print("Invalid operator")
        exit()

# 12 + 24


try:
    operand1, operator, operand2 = input("Enter Expression- ").split()
    result = arthematic_operation(int(operand1), operator, int(operand2))
    print(f"{operand1} {operator} {operand2} = {result}")
except Exception as e:
    print(f"error: {e}")
