def generator(lst):
    for i in lst:
        yield i

f1 = generator([1,2,3,4,5])

for i in f1:
    print(i)
    
f2 = generator("hello")
for i in f2:
    print(i)