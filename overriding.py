class Base:
    def calculate(self):
        self.n1=eval(input("Enter n1 :"))
        self.n2=eval(input("Enter n2 :"))
        self.add=self.n1+self.n2
    def display(self):
        print("addition :",self.add)


class Derive(Base):
    def calculate(self):
        Base.calculate(self)
        self.mul=self.n1*self.n2
    def display(self):
        Base.display(self)
        print("Mul is :",self.mul)

D=Derive()
D.calculate()
D.display()
