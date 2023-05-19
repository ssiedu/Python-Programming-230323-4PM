file=open("Emp.txt","w")
n=int(input("Enter Limit of records :"))
for i in range(n):
    name=input("Enter Employee Name :")
    E_id=int(input("Enter Employee Id :"))
    sal=eval(input("Enter Employee salary :"))
    data= str(E_id) +" | "+name+" | "+ str(sal)+ "\n"
    file.write(data)
file.close()
