def mapexample(a,b):
    return a+b

x = map(mapexample,("a","b","c"),("x","y","z"))
print(list(x))