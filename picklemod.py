import pickle
class Student:
    def __init__(self,rno=0,name=" "):
        self.rno=rno
        self.name=name
        self.s1,self.s2,self.s3=0.0,0.0,0.0
    def getMarks(self):
        print("Enter Marks of Student :")
        self.s1=eval(input("Enter subject1 marks :"))
        self.s2=eval(input("Enter subject2 marks :"))
        self.s3=eval(input("Enter subject3 marks :"))
    def display(self):
        print("Student Information :")
        print("Student Roll No. :", self.rno)
        print("Student Name     :", self.name)
        print("Subject1 Marks   :", self.s1)
        print("Subject2 Marks   :", self.s2)
        print("Subject3 Marks   :", self.s3)


S1=Student(101,"Ram")
S2=Student(102,"Shyam")
S1.getMarks()
S2.getMarks()
file=open("StudentRecord","wb")
pickle.dump(S1,file)
pickle.dump(S2,file)
file.close()

S=Student()
file=open("StudentRecord","rb")
try:
    while True:
        S=pickle.load(file)
        S.display()
except:    
    file.close()





        
