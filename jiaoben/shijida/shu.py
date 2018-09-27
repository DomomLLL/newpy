import queue
x =1
q = queue.Queue()
with open('shijiuda.txt') as f:
        while 1:
            r = f.readline()
            q.put(r)
x = 1
for j in range(200):
    for i in range(100):
        with open('{}.txt'.format(x),'a+') as l:
                l.write(q.get())
        if i == 99:
            x+=1
