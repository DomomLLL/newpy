class Fui():
    def __init__(self, longg=0, wide=0):
        self.__longg = longg
        self.wide = wide
    def mianji(self):
        return self.__longg * self.wide
    def get(self): 
        return 'long = {}, wide = {}'.format(self.__longg, self.wide)
f1 = Fui(3, 4)
print(f1.mianji())
print(f1.wide)
print(f1.get())
class Zheng(Fui):
    def mianji2(self):
        return self.wide**2
    def mianji(self):
        return self.wide * self.wide
f2 = Zheng(3, 5)
print(f2.mianji2())
print(f2.mianji())
