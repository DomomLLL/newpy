with open('shijiuda.txt') as f:
    r = f.readlines()
    count = 1
    c = 0
    for j in r:
        if count <c*101:
            count += 1
            with open('/mnt/share/shijiuda/{}.txt'.format(count),'a+') as l:
                l.write(j)
        else:
            c += 1
