class Temp:
    age = 12

    def __init__(self, name):
        self.name = name

    @staticmethod
    def temp(self):
        self.age = 20

    @classmethod
    def temp2(cls, name):
        return cls(name)


class Temp2(Temp):
    pass


abc = Temp2.temp2("karan")
print(abc.name)
