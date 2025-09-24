import re

# not starts with hello -> None
print(re.match("hello", 'this is my hello world program')) 

print(re.match("hello", 'hello,this is my hello world program'))

# case insensitive matching
print(re.match(
    "hELLo", 'HELLO,this is my hello world program', re.IGNORECASE
    ))

