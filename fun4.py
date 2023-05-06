import math
def Area():
    radius=eval(input("Enter Radius of circle :"))
    area = math.pi*radius*radius
    #print("Area of circle :%.2f" %area)
    return area


#print(Area())
#a=Area()
print("Area of circle : %.2f" %Area())
