def add_method(cls):
    print("Inside the class decorator")

    def greet(self):
        print(f"Hello, {self.name}")

    cls.greet = greet
    return cls


@add_method
class Myclass:
    def __init__(self, name):
        self.name = name


class_obj = Myclass("anurodh")
print(class_obj.name)
class_obj.greet()
