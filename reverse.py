num=int(input("Enter any number "))
temp=num
rev=0
tod=0
sod=0
while num!=0:
    rev=rev*10+num%10
    sod=sod+num%10
    tod=tod+1
    num=num//10

print("reverse number :",rev)
print("Total number of digit :", tod)
print("sum of digit :",sod)
if temp==rev:
    print("Number is pallindrome")
else:
    print("number is not pallindrome")
