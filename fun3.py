def Addition():
    num1=eval(input("Enter First Number :"))
    num2=eval(input("Enter second Number :"))
    add=num1+num2
    print("Sum is : ",add)


n=int(input("Enter Limit :"))
for i in range(n):
    Addition()
