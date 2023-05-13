class Rect:
    def __init__(self):
        self.l=2
        self.b=3.2
    def calculate(self):
        self.area=self.l*self.b
    def display(self):
        print("Area of rectangle :",self.area)


R=Rect()
R.calculate()
R.display()
