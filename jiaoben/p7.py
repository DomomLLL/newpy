class Sj():
    def __init__(self, x, y, z):
        if x + y > z and x + z > y and y + z > x:
            self.__x = x
            self.__y = y
            self.__z = z
        else:
            raise TypeError
    def get(self):
        return self.__x, self.__y, self.__z
    def mianji(self):
        import math
        t = math.sqrt(self.__y**2 -(self.__x**2)/2)
        total = t * self.__y / 2
        return total
f1 = Sj(3,4,5) 
print(f1.get())
print(f1.mianji())
