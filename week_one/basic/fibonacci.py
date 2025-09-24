# 0,1,1,2,3,5,8,13,21

try:
    num = int(input("enter number"))
    if num < 1:
        print("Invalid number")
        exit()

    a = 0
    b = 1
    print(a)
    if num == 1:
        exit()
    print(b)
    for i in range(3, num+1):
        cur = a + b
        a = b
        b = cur
        print(cur)

    # while num >= 3:
    #     cur = a + b
    #     a = b
    #     b = cur
    #     print(cur)
    #     num -= 1


except Exception as e:
    print(f"error:{e}")
