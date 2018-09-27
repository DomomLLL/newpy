x = range(1,100)
a = 0
for i in x:
    if int(i)%3 == 0 or  int(i)%5 == 0:
        a = i+a
    print(a)
