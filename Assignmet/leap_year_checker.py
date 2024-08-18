year = int(input("Enter a year : "))
is_leap = "Leap" if year%400 == 0 or year%4==0 and year%100!=0 else "Not a leap"

print(year,"is ",is_leap)