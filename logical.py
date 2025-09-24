# String Compression – Convert "aaabbcddd" → "a3b2c1d3".

# Anagram Checker – Check if two strings are anagrams (ignore spaces/case).

# First Non-Repeating Character – "swiss" → "w".

# Balanced Brackets – "([{}])" → True, "([)]" → False.

string = list('abc')
# print(string)
countingObj={}
for i in string:
    if i in countingObj.keys() :
        countingObj[i]=countingObj[i]+1
    else:
        countingObj[i]=1

compressionString=[]

for i in countingObj.keys():
    compressionString.append(i+str(countingObj[i]))

print(''.join(compressionString))