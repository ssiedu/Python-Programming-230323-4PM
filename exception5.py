try:
    num=int(input("Enter any number upto 100:"))
    if num>100:
        raise ValueError

except ValueError:
    print("Number is out of range")

else:
    print("Number is in range")
