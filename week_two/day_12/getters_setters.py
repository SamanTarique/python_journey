class BankAccount:

    branch_name = "Bapat Square"
    _manager = "aman singh"
    __bank_name = "State Bank of India"

    def __init__(self):
        self.__firstname = ""
        self.__age = ""

    @property
    def user_details(self):
        """ getter to get user firstname """
        return self.__firstname, self.__age

    @user_details.setter
    def user_details(self, details: tuple):

        if len(details) != 2:
            raise ValueError("Need firstname and age")

        firstname, age = details

        """ setter to update user firstname and age"""
        if not firstname or len(firstname.strip()) < 3:
            raise ValueError(
                "User firstname should be atleast of length 3 char"
                )
        self.__firstname = firstname.strip()

        """ setter to update user's age """
        if not age or age < 18:
            raise ValueError("User age should be atleast 18")
        self.__age = age


try:
    user1 = BankAccount()
    user1.user_details = "anurodh", 22
    user = user1.user_details
    print(f"User's Firstname - {user[0]} Age - {user[1]}")

    print(user1._BankAccount__bank_name)
    user1._BankAccount__bank_name = 'sbi'

    print(user1._BankAccount__bank_name)

except Exception as e:
    print(f"error: {e}")
