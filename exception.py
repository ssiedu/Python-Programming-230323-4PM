try:
    a=int(input("Enter First Value :"))
    b=int(input("Enter Second Value :"))
    c=a/b
    

except ZeroDivisionError:
    print("Zero Division Error")

except ValueError:
    print("Value Error")

except:
    print("server Not found")

