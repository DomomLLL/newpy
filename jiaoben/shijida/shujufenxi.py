with open('shijiuda.txt',encoding = 'utf-8') as f:
    r = f.readlines()
    count = 1
    c = 0
    for j in r:
        c += 1
        if c <= count*100:
            with open('{}.txt'.format(count),'a+',encoding = 'utf-8') as l:
                    l.write(j)
        else:
                count += 1

