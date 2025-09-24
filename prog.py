print("Enter temprature in Celcius- ")
userInputs=[]
for i in range(1):
    while True:
        try:
            userInputs.append(int(input("enter intger")))
            break
        except ValueError:
            print("Invalid integer value")
print(f"user entered values- {userInputs}")

print(f"Temprature in farenheit - {(userInputs[0]*9/5)+32}")