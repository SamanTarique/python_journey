import random

class Rock_paper_scissor:
    actions = ['Rock', 'Paper', 'Scissor']

    def random_index():
        return random.randint(0, 2)

    @staticmethod
    def get_action():
        index = Rock_paper_scissor.random_index()
        return Rock_paper_scissor.actions[index]
    
    @staticmethod
    def round_result(user_1_action, user_2_action):
        


class User(Rock_paper_scissor):

    def __init__(self, username):
        self.username = username
        self.__score = 0

    @property
    def user_score(self):
        return self.__score


user1, user2 = input("enter user name- ").split()
User_One = User(user1)
User_Two = User(user2)

# print(User_One.username, User_One.user_score)
# print(User_Two.username, User_Two.user_score)

print("***************************************************")
print("***************************************************")

for i in range(1, 6):
    print(f"Round {i} starts:")
    User_One_action = Rock_paper_scissor.get_action()
    User_Two_action = Rock_paper_scissor.get_action()
    print(
        f"{user1} move - {User_One_action} ,"
        f"{user2} move - {User_Two_action}\n"
        )
