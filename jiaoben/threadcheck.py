import subprocess
import threading
import re
class checkcp():
    def __init__(self):
        subprocess.call('ls -l',shell = True,stdout = open('threadt.py','w'))
        with open('threadt.py','r') as f:
            self.r = f.readlines()
    def getbigname(self):
        rfun = r'root\s+(\d*)\s+.+?(\w+.py)'
        size = re.findall(rfun,'{}'.format(self.r))
        big_name = []
        for i in size:
            if int(i[0])>500:
                big_name.append(i[1])
        return big_name
a = checkcp()
print(a.getbigname())
