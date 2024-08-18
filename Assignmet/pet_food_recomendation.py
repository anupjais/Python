animal = input("Enter your species : ").capitalize()
age = int(input("Enter age : "))

# food = "Senior \'"+animal+"\' food" if age>5 else "Junior \'"+animal+"\' food"
food = "Adult food" if (animal=="Dog" and age>2) or (animal=='Cat' and age>5) else "Puppy food" 
print(food)