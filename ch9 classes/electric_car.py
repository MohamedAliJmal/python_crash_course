from car import Car
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self,name,model,year):
        super().__init__(name,model,year)
        self.battery=Battery()
        
class Battery:
    def __init__(self):
        self.battery_size=75
    def describe_battery(self):
        print(f"battery size is {self.battery_size}")
    def upgrade_battery(self):
        if self.battery_size<100:
            self.battery_size=100

my_car=ElectricCar('tesla', 'model s', 2019)
my_car.battery.describe_battery()
import random