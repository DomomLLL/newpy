def f(x):
    import random
    import string
    s = string.ascii_letters
    z = []
    for i in range(x):
        q = random.randint(1,2)
        if q == 1:
            y = random.randint(0,10) 
            z.append(y)
        else:
            y = random.choice(s)
            z.append(y)
    return z
print(f(8))
