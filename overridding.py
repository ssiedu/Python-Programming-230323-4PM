class First:
    def __init__(self):
        print("This is First Class display Method")


class Second(First):
    def __init__(self):
        super().__init__()
        print("This is Second Class Display Method")




S=Second()
#S.display()
