with open("guests.txt","a") as f:
    f.write("\n")
    print("click q if you want quit")
    name=input("what s your name: ").title()
    while name!="Q":
        f.write(f"{name} \n")
        print("click q if you want quit")
        name=input("what s your name: ").title()
        