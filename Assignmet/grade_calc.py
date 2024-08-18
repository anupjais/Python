score = int(input("Enter you grade : "))

if score > 100:
    print("Please Verify your score")
    exit()
grd = "A" if score>89 else "B" if score > 79 else "C" if score>69 else "D" if score>59 else "F"

print(grd)

# if score >= 90:
#     grd = "A"
# elif score >=80:
#     grd = "B"
# elif score >=70:
#     grd = "C"
# elif score >=60:
#     grd = "D"
# else:
#     grd = "F"

# print(grd)