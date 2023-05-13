class Base1:
    def getNum1(self):
        self.l=eval(input("Enter length of rectangle :"))

class Base2:
    def getNum2(self):
        self.b=eval(input("Enter breadth of rectangle :"))

class derive(Base1,Base2):
    def calculate(self):
        self.area=self.l*self.b
        print("Area of rectangle :",self.area)


d=derive()
d.getNum1()
d.getNum2()
d.calculate()
