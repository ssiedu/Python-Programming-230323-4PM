try:
    num=int(input("Enter any number upto 100:"))
    assert num%2==0
        
except:
    print("Number is out of range")

else:
    rec=1/num;
    print("Reciprocal of number :",rec)
