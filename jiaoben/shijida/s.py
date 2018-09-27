import jieba
import re
def datasplite():
    with open('shijiuda.txt') as f:
        x = 1
        t = True
        while t:
            for i in range(100):
                r = f.readline()
                if r == '':
                    t = False
                else:
                    with open('{}.txt'.format(x),'a+') as p:
                        p.write(r)
                if i == 99:
                    x += 1 
def map(file_name):
    dic ={}
    with open('{}'.format(file_name),encoding = 'utf-8') as f:
        r = f.readlines()
    for i in r:
        seg_list = jieba.cut(i)
        ct = 1
        for j in seg_list:
            rfun = r'.*[^。，、“”:;\n].*'
            k = re.findall(rfun,j)
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1
    l = []
    for k,v in dic.items():
        l.append(k+' '+str(v)+' '+ '\n')
    with open('All.txt','a+') as fi:
        fi.writelines(l)
def check():
    rfun = r'(.*)\s\d+\s'
    rfu = r'.*?\s(\d+)\s'
    with open('All.txt',encoding = 'utf-8') as f:
        r = f.readlines()   
    for i in r:
        sss = re.findall(rfu,'{}'.format(i))
        print(sss[0])
c = check()
