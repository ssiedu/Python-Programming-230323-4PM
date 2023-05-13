class Rect:
    def __init__(self,length=1,breadth=2):
        self.l=length
        self.b=breadth
    def calculate(self):
        self.area=self.l*self.b
    def display(self):
        print("Area of rectangle :",self.area)



a=eval(input("Enter length of rect :"))
b=eval(input("Enter breadth of rect :"))
R=Rect(a,b)
R.calculate()
R.display()

R1=Rect()
R1.calculate()
R1.display()
