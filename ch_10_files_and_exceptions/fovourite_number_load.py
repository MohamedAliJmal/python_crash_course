import json
with open("favourite_number.json","r") as f:
    n=json.load(f)
    print(f"your favourite number is {n}")