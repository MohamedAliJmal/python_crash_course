with open("learning_python.txt") as f:
    #print(f.read())
    l=f.readlines()
# for line in l:
#     print(line)
s=""
for line in l:
    s+=line
print(s)