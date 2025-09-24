# 1. String basics

# Count how many times the letter "a" appears in sentence.

# Convert sentence to uppercase and lowercase.

# Replace "Python" with "JavaScript".

# Find the index of the word "powerful" in sentence.

orignalString =input("enter string")

my_dist={}
for i in orignalString:
    my_dist[i]=0

for i in orignalString:
    if i in orignalString:
        my_dist[i]=my_dist[i]+1

print(my_dist)

sentance  = "hello everyone my name is anurodh"
print(sentance.upper())

string= 'Python'
string.replace('Python','Javscript')
print(string)

string='India is a Powerful country'
print(string.find('Powerful'))