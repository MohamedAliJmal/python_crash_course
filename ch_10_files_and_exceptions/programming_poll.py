with open("programming_poll.txt","w") as f:
    print("quit anytime with press q")
    reason=input("why you like programming ")
    while reason!="q":
        f.write(reason+"\n")
        print("quit anytime with press q")
        reason=input("why you like programming ")