a=int(input("Enter First number :"))#100
b=int(input("Enter Second Number :"))#200
c=int(input("Enter Third Number :"))#100

print("Logical And : ", (a>b and a!=b))#False
print("Logical And : ", (a>c and a==c))#False
print("Logical Or  : ", (a!=b or a==c))#True
print("Logical Or  : ", (a!=b or b>c))#True
print("Logical Not : ", not(a==b))#True
print("Logical And Not :", not((a>b) and not(a!=c)))#True
print("Logical Or Not : ", (not(a>c) or not(a>b)))#True
print("AND OR NOT  : ", not(not(a<b) or (c>b and a==c)))#True

      
