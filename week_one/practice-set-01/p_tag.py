try:
    def secret(input_str: list) -> str:
        # parts = input_str.split('.')

        tag = input_str[0]

        classes = ' '.join(input_str[1:])

        return f"\"<{tag} class='{classes}'></{tag}>\""

    string = input("enter string- ").split(".")
    print(secret(string))
except Exception as e:
    print(f"error:{e}")

# print(secret("p.one.two.three"))
# print(secret("p.one"))
# print(secret("p.four.five"))
