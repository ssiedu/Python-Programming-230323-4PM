import pickle
file=open("binary1.dat","wb")
list1=[10,20,30,40,50]
pickle.dump(list1,file)
file.close()

file=open("binary1.dat","rb")
data=pickle.load(file)
file.close()
print(data)
