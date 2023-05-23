try:
    a=int(input("Enter First Value :"))
    b=int(input("Enter Second Value :"))
    c=a/b
    
except:
    print("Except block")
    print("server Not found")

else:
    print("Else Block")
    print("value of c :",c)

finally:
    print("finally Block")
