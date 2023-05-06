def simple_interest():
    p=eval(input("Enter principle amount :"))
    r=eval(input("Enter rate of interest :"))
    t=eval(input("Enter time in year :"))
    si=(p*r*t)/100
    print("simple interest : %.2f"%si)
    total = p+si
    print("Total amount : %.2f"%total)


simple_interest()
