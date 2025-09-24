try:

    def generate_prime(start, end) -> list:
        primes = []

        for num in range(start, end + 1):
            if num > 1:
                is_prime = True

                for i in range(2, int(num**0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(num)

        return primes

    def generate_armstrong(start, end) -> list:
        armstrongs = []
        for num in range(start, end + 1):
            # how many digits number have
            order = len(str(num))

            sum_of_powers = 0
            # kept orignal number for comparision later
            temp_num = num

            while temp_num > 0:
                digit = temp_num % 10
                sum_of_powers += digit**order
                temp_num //= 10

            if num == sum_of_powers:
                armstrongs.append(num)

        return armstrongs

    start, end = map(int, input("Enter range- ").split())
    print(start, end)

    if start < 0 or end < 0 or start > end or start == end:
        print(
            "Start and End should be positive number "
            "and End should be greater than Start"
        )
        exit()

    primes = generate_prime(start, end)
    armstrongs = generate_armstrong(start, end)

    print(f"Primes in range {start} - {end} are\n {primes}")
    print(f"Armstrongs in range {start} - {end} are\n {armstrongs}")

except Exception as e:
    print(f"error: {e}")
