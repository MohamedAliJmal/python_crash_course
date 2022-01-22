with open("learning_python.txt") as f:
    content=f.read()
content=content.replace("python","c")
print(content)