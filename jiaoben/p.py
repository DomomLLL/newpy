import os
import sys
def f(path):
    for i in os.listdir(path):
        l = os.path.join(path,'{}'.format(i))
        if os.path.isdir(l):
            print(l +'/')
        else:
            print(l)
#a = f(sys.argv[1])
try: 
    print('s')
    #open('hdaundlmka')
except FileNotFoundError:
    print('1')
else:
    print('2')


