with open('KMSWHS.txt') as f:
    p = f.readlines()
count = 0
for i in p:
    print(i.find('a'))
