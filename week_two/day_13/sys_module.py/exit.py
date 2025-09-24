import sys

age = int(input("Enter age-"))

if age < 18:
    sys.exit("Under age for account opening")
else:
    print("Good to go")
