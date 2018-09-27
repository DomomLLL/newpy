def f(x):
    if x == 2:
        return 2
    elif x == 1: 
        return 1
    else:
        return f(x-2) + f(x-1)

print(f(6))
print(f(4))
print(f(7))
print(f(3))
print(f(2))
print(f(8))
    
print(f(5))
