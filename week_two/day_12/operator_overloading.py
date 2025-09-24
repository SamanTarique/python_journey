class OperatorOverloading:
    def __init__(self, x, y, my_list=""):
        self.x = x
        self.y = y
        self.my_list = my_list

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __truediv__(self, other):
        return self.x / other.x, self.y / other.y

    def __len__(self):
        return len(self.my_list)


try:
    object_one = OperatorOverloading(10, 20)
    object_two = OperatorOverloading(5, 10, [1, 2, 3, 4, 5])

    print(object_one + object_two)
    print(object_one - object_two)
    print(object_one / object_two)

    print(len(object_one))
    print(len(object_two))

    print(object_one * object_two)  # Error
except Exception as e:
    print(f"Error: {e}")
