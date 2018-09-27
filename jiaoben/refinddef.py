import re
with open('p08-4.py') as f:
    r = f.readlines()
    count = 0
print('##################################')
for i in r:
    count += 1
    rf = r"(?<=def\s)\w+\(.*\)(?=:)"
    f1 = re.findall(rf,'{}'.format(i))
    if f1 != []:
        print('Line：{}   有函数：{}'.format(count,f1))
print('##################################')
for j in r:
    rf1 = r"(\w+)\s*\=\s*\w+"
    f2 = re.findall(rf1,'{}'.format(j))
    if f2 !=[]:
        print('Line: {}   有变量：{}'.format(count,f2))
