class Area:
    def getradius(self):
        self.__r=eval(input("Enter radius of circle :"))
    def calArea(self):
        self.area=3.14*self.__r*self.__r
        print("Area of circle :",self.area)


a=Area()
a.getradius()
a.calArea()
#print("radius :",a.__r)
