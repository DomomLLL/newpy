import random
class Turtle():
    def __init__(self):
        self._x = random.randint(0,9)
        self._y = random.randint(0,9)
        self._hp = 100
    
    def move(self):
        if 1 < self._x <9 :
            nowx = self._x +random.choice([1,2,-1,-2,0])
        elif self._x <= 1:
            nowx = self._x + random.choice([1,2,0])
        elif self._x >= 9:
            nowx = self._x + random.choice([-1,-2,0])
        if 1 < self._y <9:
            nowy = self._y +random.choice([1,2,-1,-2,0])
        elif self._y <= 1:
            nowy = self._y + random.choice([1,0,2])
        elif self._y >= 9:
            nowy = self._y + random.choice([-1,0,-2])
        self._x = nowx
        self._y = nowy
        self._hp -= 1
        return (self._x, self._y)
class Fish():

    def __init__(self):
        self._x = random.randint(0,10)
        self._y = random.randint(0,10)

    def move(self):
        if 0 < self._x <10 :
            nowx = self._x +random.choice([1,-1,0])
        if 0 < self._y <10:
            nowy = self._y +random.choice([1,-1,0])
        if self._x <= 0:
             nowx = self._x + 1
        if self._x >= 10:
             nowx = self._x - 1
        if self._y <= 0:
             nowy = self._y + 1
        if self._y >= 10:
             nowy = self._y - 1
        self._x = nowx
        self._y = nowy
        return (self._x, self._y)

