try:
    def to_binary(num) -> str:
        if num == 0:
            return "0"

        binary_digits = []

        while num > 0:
            remainder = num % 2
            binary_digits.append(str(remainder))  # appending remainder
            num //= 2

        # binary_digits.append('0')
        binary_digits.reverse()

        return ''.join(binary_digits)

    num = int(input("Enter a number: "))
    binary = to_binary(num)
    print(f"The binary representation of {num} is: {binary}")

except Exception as e:
    print(f"error:{e}")
