# Extract just "Python" from sentence.

# Extract "amazing" using slicing.

# Reverse the whole string using slicing.

string= 'now a days Python is a very popular and amazing language'
string = string.split()
index = string.index('Python')
print(string[index])

index = string.find('amazing')
print(string[index:index+7])

print(string[::-1])
