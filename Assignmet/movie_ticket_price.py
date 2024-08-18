# day = 'Wednesday'
age = int(input("Enter you age : "))
# print("Is it {day}")
# flag = bool(input("Enter y/n : "))

price = 12 if age>17 else 8
if day == "Wednesday":
    price-=2
print(price)
    

# if age<18 and flag :
#     print("Your ticket is at \'$6\'")
# elif age<18 and flag is False :
#     print("Your ticket is at \'$8\'")
# elif age>17 and flag :
#     print("Your ticket is at \'$10\'")
# else:
#     print("Your ticket is at \'$12\'")