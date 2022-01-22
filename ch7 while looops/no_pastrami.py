sandwich_order=["tuna sandwich","pastrami","kabab","pastrami","beef","chawerma","pastrami"]
print("the deli has run out of pastrami")
finished_sandwich=[]
while sandwich_order:
    while "pastrami" in sandwich_order:
        sandwich_order.remove("pastrami")
    a=sandwich_order.pop()
    print(f"I made you {a}")
    finished_sandwich.append(a)
for i in finished_sandwich:
    print(i)
