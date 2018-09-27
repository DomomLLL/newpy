import random
while True:
    i = random.randint(1,100)
    print(i)
    x = int(input("请输入："))
    if x == i:
        b = input('是否继续游戏y/n:')
        if b == 'n':
            break
        else:
            continue
    if x < i:
        print("太小了")
        x = int(input("请输入"))
    if x > i:
        print("太大了")
        x = int(input("请输入"))
