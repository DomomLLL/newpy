l = ["172.16.3.1", '172.16.1.5', '172.15.2.0', '172.16.3.1', '172.16.3.1', '172.16.1.5']
p = {}
for i in l:
    count = 0
    for j in l:
        if i == j:
            count +=1
            y = count
            p[i] = y
        else:
            p[i] = y
print(p)
