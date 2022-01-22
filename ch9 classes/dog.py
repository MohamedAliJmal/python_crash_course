class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(f"{self.name} sit")
    def roll_over(self):
        print(f"{self.name} roll over")
pet=Dog("spike",5)
print(pet.sit())