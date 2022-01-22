class User:
    def __init__(self,name,Id,age,country):
        self.name=name
        self.id=Id
        self.age=age
        self.country=country
        self.login_attempts=0
    def describe_user(self):
        return (f"welcome {self.name.title()} welcome to our server \n your Id is {self.id} you have {self.age} and you are {self.country}")
    def increment_login_attempts(self):
        """to make increment +1"""
        self.login_attempts+=1
        return self.login_attempts
    def reset(self):
        self.login_attempts=0
        return self.login_attempts
first=User("mohamed ali jmal","0001",18,"Tunisia")
print(first.describe_user())
print(first.login_attempts)
print(first.increment_login_attempts())
print(first.reset())
