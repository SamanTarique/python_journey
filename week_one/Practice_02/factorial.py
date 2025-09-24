try:
    # 5*4*3*2*1
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        # fact = 1

        while (num > 0):
            return num * factorial(num - 1)

        # for i in range(num, 0, -1):
        #     fact *= i
        # return fact

    num = int(input("Enter Number-"))
    if num < 0:
        print("invalid number")
    else:
        print(f"factorial of {num} is {factorial(num)}")

except Exception as e:
    print(f"error: {e}")
