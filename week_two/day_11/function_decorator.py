import time

# def my_decorator(func):
#     print("inside decorator 1")
#     func()
#     print("inside decorator 2")


# @my_decorator
# def greeting():
#     print("Good Morning")

def logging_decorator(myfunc):
    def wrapper(*args):
        print(f"**inside the logging decorator at time - {time.time()}")
        myfunc(*args)
        print(f"**inside the logging decorator at time - {time.time()}")
    return wrapper


@logging_decorator
def user_details(firstname, lastname, age, email):
    print(
        f"First name - {firstname} "
        f"Last name - {lastname} "
        f"Age - {age} "
        f"Email- {email}"
        )


user_details("aman", "singh", 25, "am@gmail.com")
