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
class Admin(User):
    def __init__(self,name,Id,age,country):
        super().__init__(name,Id,age,country)
        self.prv=Priviliges()
    
class Priviliges:
    def __init__(self):
        self.privilege="you can add an post and alter"
    def show_privileges(self):
            print(self.privilege)


me=Admin("mohamed ali jmal","123","18","Tunisia")
me.prv.show_privileges()