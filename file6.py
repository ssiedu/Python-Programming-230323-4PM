list1=[]
file=open("list2.txt","w")
for i in range(5):
    name=input("Enter name :")
    list1.append(name+"\n")

file.writelines(list1)
file.close()
