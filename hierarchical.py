class Parent:
    def __init__(self):
        self.fnum=eval(input("Enter First Number :"))
        self.snum=eval(input("Enter Second Number :"))


class child1(Parent):
    def add(self):
        self.sum=self.fnum+self.snum
        print("sum is :",self.sum)


class child2(Parent):
    def sub(self):
        self.sub=self.fnum-self.snum
        print("sub is :",self.sub)


C1=child1()
C1.add()

C2=child2()
C2.sub()
    
