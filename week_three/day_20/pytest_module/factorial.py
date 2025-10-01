def factoraial(num):
    if num == 0 or num == 1:
        return 1

    sum = 1

    while num > 0:
        sum *= num
        num = num - 1

    return sum


print(factoraial(3))
