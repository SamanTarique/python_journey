# def count(num):
#     for i in range(num):
#         yield i


# counter = count(10**6)
# print(counter)
# print(next(counter))
# for i in counter:
#     print(i)

# gen_exp = (i * i for i in range(100))
# print(next(gen_exp))
# print(next(gen_exp))
# print(next(gen_exp))

"""Countdown generator"""
# gen_exp = (i for i in range(10, -1, -1))
# for i in gen_exp:
#     print(i)


"""Even Numbers"""
# gen_exp = (i for i in range(100) if i % 2 == 0)
# print(next(gen_exp))
# print(next(gen_exp))
# print(next(gen_exp))
# print(next(gen_exp))
# print(list(gen_exp))


"""Fibonacci Number"""


# def fibo():
#     a, b = 0, 1

#     while True:
#         yield a
#         a, b = b, a + b


# fib_gen = fibo()

# for i in range(10):
#     print(next(fib_gen))


"""Infinite sequence of odd numbers"""
# gen_exp = (i for i in "inf" if i % 2 != 0)

# print(next(gen_exp))


"""Square with condition"""

gen_exp = (i * i for i in range(1, 101) if i % 2 == 0 and i * i % 5 == 0)
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
