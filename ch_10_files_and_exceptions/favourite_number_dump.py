import json
with open("favourite_number.json","w") as f:
    n=int(input("your favourite number "))
    json.dump(n,f)