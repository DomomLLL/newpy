import threading
import time
def func(name ,n):
    for i in range(n):
        print(name,i)
        time.sleep(0.5)
t1 = threading.Thread(target =func,args = ('t1',5))
t2 = threading.Thread(target = func,args =('t2',50))
t3 = threading.Thread(target = func,args = ('t3',10))
t1.start()
t1.join()
print(t3.isAlive())
t2.daemon = True
t2.start()
print('t2 name',t2.getName())
print('t2 setname',t2.setName('dasd'))
print('t2 name',t2.getName())
t3.start()
print(t3.isAlive())
t3.join()
print('main end')

