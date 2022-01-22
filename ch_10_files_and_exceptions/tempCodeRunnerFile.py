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