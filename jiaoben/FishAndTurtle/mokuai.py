x = [o for o in range(10)]
y = [p for p in range(10)]
import random
class Fish():
    def __init__(self):
        pass
    def getposition(self, i, j):
        self.position = x[i],y[j]
        e = random.randint(0,2)
        r  = random.randint(0,2)
        if e == 0:
            if i == 0:
                i = i+1
            else:  
                i = i - 1
        elif e == 1:
            if i == 9:
                i = i - 1
            else:
                i = i + 1
        elif i == 2:
            i = i
        elif r == 0:
            if j == 0:
                j = j+1
            else:
                j = j - 1
        elif r == 1:
            if j == 9:
                j = j - 1
            else:
                j = j + 1
        elif r == 2:
            j = j
        return self.position
    def die(self):
        if self.position == x.position:
            pass

class Turtle():
    i = 0
    j = 0
    def __init__(self,hp=100):
        self.hp = 100
    def getposition(self):
        start = x[i],y[j]
        e = random.randint(0,2)
        r  = random.randint(0,2)
        t = random.randint(1,3)
        if e == 0:
            if i == 0:
                i = i+1
            else:
                i = i - 1
        elif e == 1:
            if i == 9:
                i = i - 1
            else:
                i = i + 1
        elif i == 2:
            i = i
        elif r == 0:
            if j == 0:
                j = j+1
            else:
                j = j - 1
        elif r == 1:
            if j == 9:
                j = j - 1
            else:
                j = j + 1
        elif r == 2:
            j = j
        self.position = x[i],y[j]
        return self.position

    def ack(self,x):
        if self.position == x.position:
            self.hp + 10
t1 = Turtle()
while 1:
    print(t1.getposition())

