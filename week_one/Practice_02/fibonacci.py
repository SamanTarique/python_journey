try:

    def print_fibonacci(num):

        start1 = 0
        start2 = 1
        series = []
        # print(start1)
        series.append(start1)
        if num == 1:
            return
        # print(start2)
        series.append(start2)
        for i in range(3, num + 1):
            cur = start1 + start2
            start1 = start2
            start2 = cur
            # print(cur)
            series.append(cur)
        return series

    num = int(input("print fibonacci series upto _ number "))

    if num < 1:
        print("Invalid Number")
    else:
        print(' '.join(map(str, print_fibonacci(num))))

except Exception as e:
    print(f"error:{e}")
