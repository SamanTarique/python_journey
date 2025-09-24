try:
    num = int(input("enter a number"))

    print(bool(num % 2 == 0))

except Exception as e:
    print(f"Error occured: {e}")
