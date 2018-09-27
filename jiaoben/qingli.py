import os
def f(path):
    total = os.listdir(path)
    for i in total:
        l = os.path.join(path,'{}'.format(i))
        if 'tmp' in i:
            print(l)
            os.remove(l)
f('/mnt/share')
