import re

string = "hello my name is anurodh, i am doing great"
# my_list = ["name", "anurodh", "great"]
# subs = "-"

# # # print(re.match("^[{i}\??]$", string))
# # for i in string:
# #     print(re.search("^[a-z]$", string))

# # print(re.search("[0-9][0-9][0-9]", "foo456ba765r"))
# # print(re.search("[0-9][0-9][0-9]", "12foo34"))
# iterator = re.finditer("[0-9][0-9[0-9]", "foo456ba765r")

# # iterator = re.finditer(r"[^\w\\?]$", string)
# iterator = re.finditer(r"\w+", string)
# dsasl = [(i.start(), i.end()) for i in iterator if i.group() in my_list]

# lis = string.split()
# print(lis)


string = "this is a Good day to trek over the good mountains, what do you say?"
rep = ["Good", "trek", "what", "say"]
sub = "*"

for word in rep:
    if word.lower() in string: