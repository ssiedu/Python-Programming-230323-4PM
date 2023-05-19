list1=["apple\n","banana\n","kiwi\n","mango\n","orange\n"]
file=open("list1.txt","w")
file.writelines(list1)
file.close()
