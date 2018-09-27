#随机产生100个100以内的整型数，存贮在列表中，并统计偶数个数
import random
l = []
count = 0
for x in range(0,100):
    x = random.randint(0,100)
    l.append(x)
    if x%2 == 0:
        count+=1
print('总共{}个偶数'.format(count))   
print(l)
