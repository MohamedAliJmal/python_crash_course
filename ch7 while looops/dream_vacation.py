active_answer=True
dream_vacation={}
name=input("whats your name\n")
destination=input("If you could visit one place in the world, where would you go? \n")
dream_vacation[name]=destination
np=input("did want continue (yes/no) \n")
if np.lower()=="no":
    active_answer=False
while active_answer:
    name=input("whats your name\n")
    destination=input("If you could visit one place in the world, where would you go?\n")
    dream_vacation[name]=destination
    np=input("did want continue (yes/no)\n")
    if np.lower()=="no":
        active_answer=False
for name,destination in dream_vacation.items():
    print(f"{name.title()} wants to go to {destination.title()}")   
