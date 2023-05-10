class Largest:
    def getdata(self):
        self.fnum=int(input("Enter First Number :"))
        self.snum=int(input("Enter Second Number :"))
    def large(self):
        if self.fnum>self.snum:
            #print(self.fnum," is greater")
            return self.fnum
        else:
            #print(self.snum," is greater")
            return self.snum



L=Largest()
L.getdata()
#res=L.large()
print("largest number :",L.large())
