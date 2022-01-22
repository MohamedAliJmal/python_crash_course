import json

def get_name():
    try:
        with open("user.json") as f:
            name=json.load()
            return name
    except FileNotFoundError:
        return None

def new_user():
    with open("user.json","w") as f:
        name=input("what s your name")
        json.dump(name,f)
        return name
def greet_user():
    """greet the user"""
    name=get_name()
    if name:
        print(f"welcome back {name}")
    else:
        name=new_user()
        print(f"We\'ll remember you when you come back, {name}!")
greet_user()