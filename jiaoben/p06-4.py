def f(x):
    count = 0
    for i in range(1, x):
        if x%i == 0:
            count += 1
    if count == 1:
        return '是质数 ' 
        print(count)
    else:
        return '不是质数' 
print(f(4))  
print(f(7))  

