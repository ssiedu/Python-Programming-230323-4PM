while True:
    ch=input('''
start calculator
1.Yes(y|Y)
2.Exit(e|E)
''')
    if ch.lower()=='y':
        var=input('''
1.Addition(+)
2.Subtraction(-)
3.Multiplication(*)
4.Division(/)
5.Modulus(%)
Enter Your Choice : ''')

        fnum=eval(input("Enter First Number :"))
        snum=eval(input("Enter Second Number :"))

        match var:
            case '+':
                add=fnum+snum
                print("Sum is :",add)
            case '-':
                sub=fnum-snum
                print("Sub is :", sub)
            case '*':
                mul=fnum*snum
                print("Mul is :", mul)
            case '/':
                div=fnum/snum
                print("Div is :",div)
            case '%':
                mod=fnum%snum
                print("Mod is :",mod)
            case _:
                print("Please Enter Valid Choice ")
    else:
        break;
    
    

