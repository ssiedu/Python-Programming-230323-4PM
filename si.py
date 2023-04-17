p=eval(input("Enter principle amount:"))
r=eval(input("Enter Rate of interest :"))
t=eval(input("Enter time in year :"))
si=(p*r*t)/100
print("Simple interest :%.2f"%si)
total=p+si
print("Total amount:",total)
