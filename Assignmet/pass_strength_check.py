passw = input("Enter your password : ")
stren = "Strong" if len(passw)>10 else "Weak" if len(passw)<6 else "Medium"
print("Your password is",stren)