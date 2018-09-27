class Jisuan():
    men = ''
    day = ''
    def jiejiari(self):
        if self.day == 'hoilday':
            return  120
        else:
            return 100
    def renshu(self, x):
        return x
    def panduan(self, x):
        if self.men == 'student':
            return self.jiejiari()*0.5*self.renshu(x)
        else:
            return self.jiejiari()*self.renshu(x)
f1 = Jisuan()
f1.men = 'student'
f1.day = 'hoilday'
print(f1.panduan(1))
f2 = Jisuan()
print(f2.panduan(2))
