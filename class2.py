class Addition:
    def getdata(self):
        self.fnum=eval(input("Enter First Number :"))
        self.snum=eval(input("Enter Second Number :"))
    def calculate(self):
        self.add=self.fnum+self.snum
    def display(self):
        print("Sum is :",self.add)


A=Addition()
A.getdata()
A.calculate()
A.display()

A1=Addition()
A1.getdata()
A1.calculate()
A1.display()
