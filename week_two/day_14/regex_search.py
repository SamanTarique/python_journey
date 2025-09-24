import re

# s = 'foo123bar'

# One last reminder to import!

# print(re.search('123', s))
# print(re.search('[0-9][0-9][0-9]', 'foo456bar'))
# print(re.search('[0-9][0-9][0-9]', '12foo34'))

# The dot (.) metacharacter matches any character except a newline
# print(re.search('1.3', 'foo13hg'))
# print(re.search('1.3', 'foo123hg'))


# print(re.search('bar[ace]', 'bare'))
# ^ -> starting of the string , + -> one or more char
#  * -> zero or more char , $ -> end of the string
print(re.search('^[a-z]', 'hero'))
print(re.search('^[a-z]*', ''))
print(re.search('^[a-z]+[A-Z]*$', 'heroO'))


print(re.search('^[0-9][0-9]$', 'abc12'))
print(re.search('^[a-z]*[0-9]+[a-z]*$', 'abc123'))

# ^ inside the brackets → negation: match any character not listed(a-z).
print(re.search('[^a-z]', 'a@23'))


print(re.search('[a-z-]', '---'))
print(re.search('[a-z^-]', '098^89'))
print(re.search('[a-z\-^]', '098-89'))


print(re.search('[\w\s]', '--12as'))

# '.' works as a meta character which means
#  every character except new line character

# '\.' works as a literal character in the string,
# and returns the span of where it starts and ends
print(re.search('.', 'anurodh.kumar'))
print(re.search('\.', 'anurodh.kumar'))

# ? -> either zero or one occurences of character comes before ?
print(re.search('anux?kum', 'anukum'))
print(re.search('anux?kum', 'anuxkum'))
print(re.search('anux?kum', 'anu kum'))
print(re.search('anux?kum', 'anuskum'))

# ? says only one or zero occurences , here 42 is 2 occurences of digits
print(re.search('foo[0-9]?bar', 'foo42bar'))
print(re.search('foo[0-9]?bar', 'foo4bar'))