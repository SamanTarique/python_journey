import re

# Validate Email

regex = '^[a-zA-Z0-9_-]{3,25}@[a-zA-Z0-9.-]{2,50}\.[a-zA-Z]{2,20}$'

print(re.match(regex, 'zukku@fb.com'))
print(re.match(regex, 'ab@gmail.com'))

# Validate Phone number

regex = '^\+?[\d]{5,15}$'
print(re.match(regex, '9899'))
print(re.match(regex, '90899'))
print(re.match(regex, 'abcdefg'))
print(re.match(regex, '99009898768876578'))

# validate username

regex = '^[a-zA-z]{3,20}[\w\.\-!@#$%^&*]*$'

print(re.match(regex, 'ar'))
print(re.match(regex, 'arpit'))
print(re.match(regex, '123456'))
print(re.match(regex, '@##@#@#'))
print(re.match(regex, 'anurodh123'))