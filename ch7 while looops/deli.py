sandwich_order=["tuna sandwich","kabab","beef","chawerma"]
finished_sandwich=[]
while sandwich_order:
    a=sandwich_order.pop()
    print(f"I made you {a}")
    finished_sandwich.append(a)
for i in finished_sandwich:
    print(i)
