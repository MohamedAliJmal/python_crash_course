class Restaurant:
    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
    def describe(self):
        return f"our lovely restaurant{self.name.title()} is a tunisian restaurant "
    def open_time(self):
        return "we open from 10am to 12pm"
my_restaurant=Restaurant("fathila","Tunisian type")
print(my_restaurant.name.title())
print(my_restaurant.cuisine_type)
print(my_restaurant.describe())
print(my_restaurant.open_time())