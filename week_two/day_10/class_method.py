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
    def valid_numbers(*num):
        for i in num:
            if isinstance(i, int):
                return True
            else:
                raise ValueError(f"Invalid input value {i}")


class Rbi:
    instance = []

    def __init__(self, name, dob, pan):
        self.name = name
        self.dob = dob
        self.pan = pan
        self.instance.append(self)

    @classmethod
    def create_account(cls, name, dob, pan):
        # print(MathOperations.valid_numbers(6))
        return cls(name, dob, pan)


try:
    rbi1 = Rbi.create_account("anu", "1/1/1", "fsgdhfj")
    rbi2 = Rbi.create_account("anu", "1/1/1", "fsgdhfj")
    rbi3 = Rbi.create_account("anu", "1/1/1", 3)

    print(len(Rbi.instance))

except Exception as e:
    print(f"error: {e}")
