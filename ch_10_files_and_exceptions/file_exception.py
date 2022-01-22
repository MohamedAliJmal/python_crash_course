try:
    with open("alice.txt") as f:
        f.read()
except FileNotFoundError:
    print("file doesn\' exists")