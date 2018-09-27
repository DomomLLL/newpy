li = [1,2,3,'a','b','4','c']
dic = {}
a = []
count = -1
if ('k5') not in dic.keys():
    for i in li:
        count += 1
        if count%2 == 1:
            a.append(i)        
    dic['k5'] = a
    print(dic)
else:
    print(0)
