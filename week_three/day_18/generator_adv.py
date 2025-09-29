def primes():
    num = 2

    while True:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                continue
        yield num
        num += 1


gen_exp = primes()

for _ in range(10):
    print(next(gen_exp))
