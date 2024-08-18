import math
def cir_area(radius):
    area = math.pi * radius**2
    circum = 2*math.pi*radius
    return area, circum

area, circum = cir_area(4)

# print("{:.2f}".area)
print("{:.4f}".format(area))
print("{:.2f}".format(circum))