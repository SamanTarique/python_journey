try:

    def is_prime(num) -> bool:

        if num < 2:
            return False

        # prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
                # prime = False
                # break
        return True

    num = int(input("input number"))

    print(is_prime(num))


except Exception as e:
    print(f'error: {e}')
