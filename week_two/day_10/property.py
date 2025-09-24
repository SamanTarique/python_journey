class Person_info:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.__account_number = ''
        self.__pan = ''

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    @property
    def pan_number(self):
        return self.__pan

    @pan_number.setter
    def pan_number(self, pan):
        self.__pan = pan

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.account_number}"

    @pan_number.deleter
    def pan_number(self):
        del self.__pan


person = Person_info("anurodh", "kumar")
print(person.account_number)
person.account_number = 12312312312
print("*********************************")
print(person.account_number)
print(person.pan_number)
print("*********************************")
person.pan_number = 'HJHG75675674'
print(person.pan_number)
print("*********************************")
del person.pan_number
print(person.__dict__)