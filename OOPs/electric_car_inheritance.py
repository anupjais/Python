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

class Electric(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_car = Electric("Tesla","Cyber Truck","2000kWh")
print(my_car.display())
print(my_car.battery_size)