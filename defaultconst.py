class Rect:
    def getdata(self):
        self.l=eval(input("Enter the length of rectangle :"))
        self.b=eval(input("Enter the breadth of rectangle :"))
    def calculate(self):
        self.area=self.l*self.b
    def display(self):
        print("Area of rectangle :",self.area)


R=Rect()
R.getdata()
R.calculate()
R.display()
