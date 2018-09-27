import random
l = []
for i in range(0,10):
    a = input('请输入姓名：')
    l.append(a)
print('参选人有：', l)
print('队长是{}'.format(random.choice(l)))
