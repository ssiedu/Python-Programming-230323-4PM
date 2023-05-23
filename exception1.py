try:
    a=10
    b=0
    c=a/b
    print(c)

except ZeroDivisionError:
    print("404 Error :some Error Occured")

except TypeError:
    print("Type Error")
