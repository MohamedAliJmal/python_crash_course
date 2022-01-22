n1=input("first number ")
n2=input("second number ")
try:
    result=int(n1)+int(n2)
except ValueError:
    print("inputs must be digits")
else:
    print(result)
