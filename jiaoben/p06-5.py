def f(x,y):
    p = x
    count = 0
    o = 0
    for i in range(1,y):
        count += 1
        x = x+p*10**count
    o += x
    return o
print(f(3,5))
