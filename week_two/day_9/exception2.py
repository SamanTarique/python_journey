# try:
#     c = str(1) + 2
#     print(c)
# except (TypeError, ValueError) as e:
#     print(f"error: {e}")


class AgeError(Exception):
    pass


def check_age(age):
    if age <= 18:
        raise AgeError("not valid age")
    elif age > 18:
        return "valid age"
    elif age <= 0:
        raise ValueError("invalid age")


try:
    age = int(input("enter your age"))
    valid = check_age(age)
    print(f"Your age is {valid}")
except AgeError as e:
    print(f"error: {e}")
except ValueError as e:
    print(f"error: {e}")
