distance = int(input("Enter distance : "))

sugg = "Walk" if distance<3 else "Bike" if distance<15 else "Car" 

print(sugg)