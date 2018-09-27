class my_open():
    path = ''
    def __init__(self, x):
        self.path = x
    def content(self):
        file_now = open(self.path)
        content = file_now.readlines()
        count = 0
        con = {}
        for i in content:
            count += 1
            con[count] = i 
        return con
    def add(self, *joj):
        file_now = open(self.path)
        content = file_now.readlines()
        for j in joj:
            content.append('{}'.format(j))
        return content
    def __del__(self):
        print('over')
    def addlines(self,*lll):
        file_now = open(self.path)
        content = file_now.readlines()
        k = ['%s, %s' % (n, lll) for n in content]
        return k
f2 = my_open('/mnt/share/p677.py')    
print(f2.add('1','3'))
print(f2.addlines('6'))
