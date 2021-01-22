"""
This is a practice file for Dictonary
A Dictionary is a unordered changable and indexed collection of objects
"""
mydict = {0:"zero", 1:"one", 2:"two", 3:"three"}
print(type(mydict), "Size: ",len(mydict))
print(mydict)
mydict[2] = "twoo"
print(mydict)
for x in mydict:
    print(mydict[x])
for x,y in mydict.items():
    print(x,y)