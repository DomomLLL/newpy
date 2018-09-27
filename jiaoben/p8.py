
class a():
    def __init__(self):
        print('A')
class b(a):
    def __init__(self):
        print('B')
class c(a):
    def __init__(self):
        print('C')
class d(b,c):
    def __init__(self):
        pass
    @property
    def fee(self):
        return self.app
        
    @fee.setter
    def fee(self, x):
        self.app = x
s = d()

class Person():
    def __init__(self, f,l):
        self.l = l
        self.f = f
    @property
    def fullname(self):
        return '{}{}'.format(self.f, self.l)
    @fullname.setter
    def fullname(self, x):
        l = x.split()
        self.f  = l[0]
        self.l = l[1]
zhangsan = Person('zhang','san')
print(zhangsan.fullname)
zhangsan.fullname = 'li si'
print(zhangsan.fullname)

