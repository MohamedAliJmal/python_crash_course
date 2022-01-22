"""
read line by line

with open("pi_decimal.txt") as object_file:
    for line in object_file:
        print(line.rstrip())
"""
"""
storing file lines in a list than print it with for loop
with open("pi_decimal.txt") as object_file:
    lines=object_file.readlines()
print(lines)
for line in lines:
    print(line.strip())
    """
#file.readline()=>read just a line
#file.readlines()=> make a list of lines
"""
with open('pi_decimal.txt') as pi:
    l=pi.readlines()
pi_string=""
for line in l:
    pi_string+=line.strip()
print(pi_string)
print(len(pi_string))
"""