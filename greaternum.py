a=int(input("Enter First Number :"))
b=int(input("Enter Second Number :"))
c=int(input("Enter Third Number :"))
if a>b and a>c:
    print("{0} is greater than {1} and {2}".format(a,b,c))
elif b>c:
    print("{1} is greater than {0} and {2}".format(a,b,c))
else:
    print("{2} is greater than {0} and {1}".format(a,b,c))
    
