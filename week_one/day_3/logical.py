# and
age = 25
has_id = True

if age >= 18 and has_id:
    print("Allowed to enter.")
else:
    print("Entry denied.")

# or
is_student = False
has_discount_coupon = True

if is_student or has_discount_coupon:
    print("You get a discount!")
else:
    print("No discount available.")

# not
is_logged_in = False

if not is_logged_in:
    print("Please log in.")
else:
    print("Welcome back!")
