import json
from random import randint
l=[randint(1,100) for i in range(5)]
print(l)
with open("number.json","w") as f:
    json.dump(l,f)
print(l)