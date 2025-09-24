def add_attribute_decorator(cls):
    cls.class_name = cls.__name__
    return cls


@add_attribute_decorator
class Temp:
    pass


print(Temp.class_name)
