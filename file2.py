file=open("myfile2.txt","w")
name=input("Enter name of student :")
rollno= int(input("Enter roll number :"))
marks = eval(input("Enter marks : "))
file.write(name + "\t" + str(rollno) + "\t" + str(marks) +"\n")

file.close()
