class Series:
    def getNum(self):
        self.n=int(input("Enter any number :"))
        self.sum=0
    def display(self):
        print("Series is :")
        for i in range(1,self.n+1):
            print(i,end=" ")
            self.sum=self.sum+i
        print("\nSum of series :", self.sum)


S=Series()
S.getNum()
S.display()
