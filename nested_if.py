     


age = int(input("enter your age: "))
agew = int(input("enter your weight: "))

if age >= 18:
    if agew >= 50:
        print("Eligible to donate blood")
    else:
        print("Underweight")
else:
    print("Underage") 

print("Bye")
