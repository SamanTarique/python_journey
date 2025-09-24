def check_username_decorator(func):
    users = []
    print("here")

    def wrapper(*args):
        if args[0] in users:
            print(f"{args[0]} usernmae is already taken")
            return

        users.append(args[0])
        return func(*args)

    return wrapper


@check_username_decorator
def create_user(name, age, email):
    print(
        f"Name - {name} "
        f"Age - {age} "
        f"Email - {email}"
    )


create_user("anusrodh", 24, "anu@gmail.com")
create_user("anusrodh", 24, "anu@gmail.com")
