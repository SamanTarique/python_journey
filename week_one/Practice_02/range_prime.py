try:

    def prime_in_range(num1: int, num2: int) -> list:
        primes = []

        for i in range(num1, num2 + 1):
            if i > 1:
                is_prime = True

                for j in range(2, int(i**0.5) + 1):
                    if i % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(i)

        return ' '.join(map(str, primes))

    num1, num2 = map(int, input("Enter range-").split())
    if num1 == num2 or num2 < num1 or num1 < 0 or num2 < 0:
        raise ValueError("invalid input values")

    print(prime_in_range(num1, num2))
except Exception as e:
    print(f"error:{e}")
