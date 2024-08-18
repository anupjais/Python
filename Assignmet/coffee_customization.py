size = input("Enter coffee size : ").lower()
shot = input("Extra shot : ").lower()
e_shot = True if shot=="y" else False

coffee = size.capitalize()+" With extra shot" if e_shot == True else size.capitalize()

print("Coffee with",coffee)