def number_validator(func):
    print("inside number valdator-")

    def wrapper(*args):

        if len(args) != 2:
            raise ValueError("Two numbers should be given")

        for i in args:
            if not isinstance(i, int):
                raise ValueError("Invalid Value")
        result = func(*args)
        return result

    return wrapper


@number_validator
def addition(a, b):
    return a + b


try:
    print(addition(20, "dsf"))
    print(
        addition(
            20,
        )
    )
except Exception as e:
    print(f"error: {e}")
