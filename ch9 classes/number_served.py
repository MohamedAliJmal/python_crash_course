class Restaurant:
    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe(self):
        return f"our lovely restaurant{self.name.title()} is a tunisian restaurant "
    def open_time(self):
        return "we open from 10am to 12pm"
    def set_number_served(self,n):
        self.number_served=n
        return self.number_served
    def increment_number_served(self):
        self.number_served+=1
        return self.number_served
my_restaurant=Restaurant("fathila","Tunisian type")
print(my_restaurant.number_served)
my_restaurant.number_served=5
print(my_restaurant.number_served)
print(my_restaurant.set_number_served(6))
print(my_restaurant.increment_number_served())