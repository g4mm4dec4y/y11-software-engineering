#---begin Python ---
class Car:
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
    
    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

# Instantiating objects from the Car class
#For each object, all the appropriate information is input as variables. 
car1 = Car("Toyota", "Camry", 2020, "Red")
car2 = Car("Honda", "Civic", 2018, "Blue")

car1.start()  # Output: Toyota Camry is starting.
car2.stop()   # Output: Honda Civic is stopping.
#--- end python ---

class ElectricCar(Car):

    def start(self):
        print(self.make + self.model + "has started and is fullycharged.")

    def start(self):
        print(f"{self.make} {self.model} is starting silently.")

    def charge_battery(self):
        print("Battery is charged")

    def original_start(self):
        super().start()
         
electric_car = ElectricCar("Tesla", "Model S", 2022, "White")

electric_car.original_start()

