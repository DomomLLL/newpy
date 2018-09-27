l = []
a = -1
for x in range(1,10):
    if x%3 == 0 or x%5 == 0:
        a += 1
        l.append(x)
        
print(l)
