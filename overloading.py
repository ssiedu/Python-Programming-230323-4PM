from multipledispatch import dispatch

@dispatch(int,int)
def product(fnum,snum):
    result=fnum*snum
    print("product of two integer :",result)


@dispatch(int,int,int)
def product(fnum,snum,tnum):
    result=fnum*snum*tnum
    print("product of three integer :",result)

@dispatch(int,float)
def product(fnum,snum):
    result=fnum*snum
    print("product of two different value :",result)

@dispatch(int,int,float)
def product(fnum,snum,tnum):
    result=fnum*snum*tnum
    print("product of three diff values :",result)


product(10,2,3)
product(10,2,2.1)
product(10,20)
product(10,2.4)







    
