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

class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine_type):
        super().__init__(name,cuisine_type)
        self.flavor=["chocalate","strawberry","psitache","Oreo"]
test=IceCreamStand("fathila","glasse wil birra")
print(test.cuisine_type)
print(test.flavor[0])

