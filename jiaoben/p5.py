x = int(input("请输入一个整数:"))
t = 0
count = 0
for i in range(1,x+1):
    count += 1
    t = t+i
    if t%count == 0:
        print('结果为{}'.format(t))

