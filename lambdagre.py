largest = lambda num1,num2: num1 if num1>num2 else num2


fnum=int(input("Enter First Number :"))
snum=int(input("Enter Second Number :"))
result=largest(fnum,snum)
print("largest number :",result)
