class Car:
    # brand
    # model
    # def __init__(self):
    #     brand = "Tata"
    #     model = "Harrier"
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model


    def display(self):
        return f"{self.brand} {self.model}"

my_car = Car("Mahindra","Thar")

# print("Brand:",my_car.brand)
# print("Model:",my_car.model)

print(my_car.display())

