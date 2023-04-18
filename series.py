n=int(input("Enter any number :"))
i=int(input("Enter start number :"))
print("Even Series:")
while i<=n:
    if i%2==0:
        print(i,end=" ")
    i=i+1
print("\nOdd Series")
print(" value of i ",i)
#i=1
while i<=n:
    if i%2!=0:
        print(i,end=" ")
    i=i+1
