try:

    def is_armstrong(num: int) -> bool:
        if num <= 0:
            return False
        else:
            num_len = len(str(num))
            temp_num = num
            sum_of_pow = 0
            while temp_num:
                digit = temp_num % 10
                sum_of_pow += digit**num_len
                temp_num //= 10
            if sum_of_pow == num:
                return True
            else:
                return False
    num = int(input("enter number "))

    print(is_armstrong(num))

except Exception as e:
    print(f"error: {e}")
