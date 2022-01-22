"""best practice first"""
class Car :
    """A simple attempt to represent a car."""
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
        self.odometer_reading = 0
        

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.name} {self.model}"
        return long_name.title()
    

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def describe_car(self):
        print(f"the car is {self.name.title()} model {self.model.title()} produced {self.year}")

