import sys

string = []

for i in sys.stdin:
    if i.rstrip() == 'q':
        break
    print(f"string -{i}")
    string.append(i)

print(string)
