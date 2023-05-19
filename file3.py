file=open("myfile3.txt","w")
n=int(input("Enter limit :"))
for i in range(n):
    name=input("Enter name :")
    file.write(name+"\n")

file.close()
