class Mylist():
    def __init__(self, *agrs):
        self.__mylist = [i for i in agrs]
    def __sub__(self,x):
        print([i-x for i in self.__mylist])
l = Mylist(1,2,34,5,6,7)
l - 3   
l.__sub__(3)
