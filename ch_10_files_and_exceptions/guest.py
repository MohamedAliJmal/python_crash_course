with open("guests.txt","w") as f:
    name=input("what\'s your name:").title()
    f.write(name)