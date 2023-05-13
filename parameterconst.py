class Rect:
    def __init__(self,length,breadth):
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
