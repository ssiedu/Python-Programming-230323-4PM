class First:
    def __init__(self):
        self.p=eval(input("Enter principle amount:"))
        self.r=eval(input("Enter rate of interest :"))
        self.t=eval(input("Enter time in year :"))


class Second(First):
    def calculate(self):
        self.si=(self.p*self.r*self.t)/100
        self.total=self.si+self.p

class Third(Second):
    def display(self):
        print("Simple Interest :",self.si)
        print("Total amount :",self.total)


T=Third()
T.calculate()
T.display()
