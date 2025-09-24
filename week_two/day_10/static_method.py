class MathOperations:
    """For utility function"""

    @staticmethod
    def sum_of_numbers(*args):
        sum = 0
        for i in args:
            sum += i
        return sum

    """For utility function"""

    @staticmethod
    def max_number(*args):
        max = -99999999
        for i in args:
            if i > max:
                max = i
        return max

    """For Validation purpose"""

    @staticmethod
    def valid_numbers(num):
        for i in num:
            if isinstance(i, int):
                continue
            else:
                raise ValueError(f"Invalid input value {i}")


class Electricity(MathOperations):

    def __init__(self, *monthly_units):
        self.monthly_units = monthly_units
        MathOperations.valid_numbers(self.monthly_units)

    def get_sum_of_units(self):
        return MathOperations.sum_of_numbers(*self.monthly_units)

    def __str__(self):
        return f"Electricity consumption (units): {self.monthly_units}"


# class temp:

#     m = MathOperations.max_number(67, 89)

try:
    c1 = Electricity(1, 2, 3, "hfdkj")
    print(c1)
    print(c1.get_sum_of_units())
    # print(c1.max_number(1, 2, 3, 4))
    print("**************************************************")
    # t = temp()
    # print(MathOperations.max_number(1, 2, 3, 4, 5))
    # print(temp.m)
    # print(MathOperations.sum_of_numbers(1,2,3,4))
except Exception as e:
    print(f"error: {e}")
