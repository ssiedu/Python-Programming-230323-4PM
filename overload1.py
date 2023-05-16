class Area:
    def findArea(self,a=None,b=None):
        if (a!=None and b!=None):
            print("area of rect :",a*b)
        elif (a!=None):
            print("square of number :",a*a)
        else:
            print("Nothing")


A=Area()
A.findArea()
A.findArea(2)
A.findArea(2,3)
