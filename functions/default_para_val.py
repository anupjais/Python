# def greet(name = "User"):
#     return "Good Morning "+name+"!"

# print(greet())
# print(greet("Ramesh"))

def greet(mode = "Morning", name = "User"):
    return "Good "+mode.capitalize()+" "+name.capitalize()+"!"

print(greet('afternoof', "ramesh"))
print(greet('evening', "pallaVi"))
print(greet("","SanDeeP"))