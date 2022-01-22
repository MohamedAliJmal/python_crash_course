while True:
    print("enter q to quite")
    first_number=input("the first number please ")
    if first_number=="q":
        break
    print("enter q to quite")
    second_number=input("the second number please ")
    if second_number=="q":
        break
    try:
        answer=int(first_number)/int(second_number)
    except ValueError:
        print("you have to enter digits")
    except ZeroDivisionError:
        print("we can t divide by zero")
    else:
        print(answer)


""" bl=True
while bl:
    print("enter q to quite")
    first_number=input("the first number please ")
    if first_number=="q":
        bl=False
    while bl:
        print("enter q to quite")
        second_number=input("the second number please ")
        if second_number=="q":
            break
        try:
            answer=int(first_number)/int(second_number)
        except ValueError:
            print("you have to enter digits")
        except ZeroDivisionError:
            print("we can t divide by zero")
        else:
            print(answer) """
