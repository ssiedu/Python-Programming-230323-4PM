def list1(**data):
    print(data)
    print(data['x'])
    print(data['y'])
    print(data['z'])
    for i,j in data.items():
        print(i,j)


list1(x=10,y=20,z=30)
