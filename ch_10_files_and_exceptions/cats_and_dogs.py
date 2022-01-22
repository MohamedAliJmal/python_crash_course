try:
    with open("cats.txt") as c:
        print(c.read())
except FileNotFoundError:
    # print("cats.txt not found")
    pass

try:
    with open("dogs.txt") as g:
        print(g.read())
except FileNotFoundError:
    # print("dogs.txt not found")
    pass