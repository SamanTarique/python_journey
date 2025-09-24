# def fact(num):
#     if num==0 or num ==1:
#         return 1
#     res=1
#     for i in range(2,num+1):
#         res*=i
#     return res


def fact(num):
    if num == 0 or num == 1:
        return 1
    res = 1
    return res * fact(num - 1)


print(fact(4))
