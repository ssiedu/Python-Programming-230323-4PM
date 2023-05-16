class Base:
    def __init__(self):
        self.l=eval(input("Enter length :"))
        self.b=eval(input("Enter breadth :"))

class Parent1(Base):
    def calRArea(self):
        self.rarea=self.l*self.b


class Parent2:
    def getdata(self):
        self.r=eval(input("Enter radius :"))
        self.carea=3.14*self.r*self.r


class child(Parent1,Parent2):
    def display(self):
        print("Area of rectangle :%.2f"%self.rarea)
        print("Area of circle    :%.2f"%self.carea)


C=child()
C.calRArea()
C.getdata()
C.display()
