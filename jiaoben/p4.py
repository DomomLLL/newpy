x = int(input("请输入一个整数:"))
t = 0
count = 0
for i in range(1,x+1):
    t += i
    for j in range(1,x+1):
        t = t+j
print(t)

