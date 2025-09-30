"""Abstraction: It is the most essential fetaure in oops which says providing
only the essential data to the outside world
and hiding the background details and complex implementation"""


class Github:
    usernames = []

    def __init__(self, first_name, last_name, username=None):
        self.first_name = first_name
        self.last_name = last_name
        self.__username = username

    @staticmethod
    def get_usernames():
        return Github.usernames

    @property
    def my_username(self):
        return self.__username

    @my_username.setter
    def my_username(self, username):
        if username in self.get_usernames():
            print(f"Username '{username}' is already taken")
            return
        self.__username = username
        Github.usernames.append(username)


user1 = Github("anurodh", "kumar")
user2 = Github("aman", "kumar")
print(user1.get_usernames())
print(user1.my_username)
user1.my_username = "idabora"
print(user1.my_username)
user2.my_username = "idabora"
