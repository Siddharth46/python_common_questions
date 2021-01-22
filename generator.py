def genexample():
    a = 1
    while a < 5:
        yield a
        a = a+1

z = genexample()
print(next(z))
print(next(z))
