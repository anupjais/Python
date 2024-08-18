print("Suppose you have a Banana")

color = (input("Enter the color of it : ").lower())

ripeness = "Overripe" if color == "brown" else "Ripe" if color == "yellow" else "Unripe" if color == "green" else "There is no Banana"
# if color=="brown":
#     ripe = "Overripe"
# elif color == "yellow":
#     ripe = "Ripe"
# else :
#     ripe="Unripe"
# print(ripe)

print(ripeness)
