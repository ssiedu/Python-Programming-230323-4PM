ch=int(input("Enter any number in between 1 to 5: "))
match ch:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case _:
        print("Invalid choice")
