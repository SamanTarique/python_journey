import re

a = 'anurodh kuamr is sitting on a chair with wheels'

print(re.split('\W', a))

b = 'here,i,am,writing,english'

print(re.split(',', b, maxsplit=2))