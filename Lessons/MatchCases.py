uInput=int(input("Enter Day Number (Monday is Starting): "))

match uInput:
    case 1:
        print("It's Monday")
    case 2:
        print("It's Tuesday")
    case 3:
        print("It's Wednesday")
    case 4:
        print("It's Thursday")
    case 5:
        print("It's Friday")
    case 6:
        print("It's Saturday")
    case 7:
        print("It's Sunday")
    case _:
       print("Enter correct Day")