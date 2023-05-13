class Base:
    def __init__(self):
        self.r=eval(input("Enter radius of circle :"))



class derive(Base):
    def calculate(self):
        self.area=3.14*self.r*self.r
        print("Area of circle :",self.area)


d=derive()
d.calculate()
