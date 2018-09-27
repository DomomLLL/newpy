import random
from m import Fish, Turtle
class main():
    def move(self):
        self.fish1 = Fish()
        self.fish2 = Fish()
        self.fish3 = Fish()
        self.fish4 = Fish()
        self.fish5 = Fish()
        self.turtle = Turtle()
        t = True
        while 1:
            self.turtle._hp -= 1
            if self.turtle.move() == self.fish1.move():
                self.turtle._hp += 10
                t = False
                return '乌龟在{}抓住了鱼'.format(self.turtle.move())
            else:
                print('鱼：{}， 乌龟：{}'.format(self.fish1.move(),self.turtle.move()))
f11 = main()
print(f11.move())
