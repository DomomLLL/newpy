for x in range(6,10000):
    a = x
    count = 0
    for i in range(5):
        if x%5==1:
            count += 1
            y = (x-1)/5
            x = x-y-1
        if count == 5:
            print(a)
         
