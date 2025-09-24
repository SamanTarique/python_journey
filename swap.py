val1,val2 = map(int,input("enter 2 integeres - ") .split())
userinputs = []
for x in range(2):
    while True:
        try:
            userinputs.append(int(input(f"enter {x+1}th integer")))
            break
        except ValueError:
            print("Invalid Integer value")

# values = [inputval(x) for x in values]
print("values- ", userinputs)
# val1=val1+val2
# val2=val1-val2
# val1=val1-val2
# print(val1,val2)