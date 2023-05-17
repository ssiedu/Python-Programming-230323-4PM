import random
while True:
    uc=input('''
Game Start....
1.Yes('y')
2.Exit('n')
''')
    if uc=='y' or uc=='Y':
        cinput=random.randrange(1,4)
        uinput=int(input("User input :"))
        if cinput>uinput:
            print("computer input :",cinput)
            print("computer input is greater than user input")

        elif uinput>cinput:
            print("computer input :",cinput)
            print("User input is greater than computer input")

        else:
            print("computer input :",cinput)
            print("Both inputs are equal")

    else:
        break;
