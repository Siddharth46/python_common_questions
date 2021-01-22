"""
This is a practice programe for tuples
A Tuple is a ordered and unchangable collection of objects
"""
mytuple = (0,"one", 2, "three")
print(type(mytuple), "len: ",len(mytuple))
print(mytuple)
print(mytuple[1])
print(mytuple[1:-1])
mylist = list(mytuple)
mylist[0] = "zero"
mytuple = tuple(mylist)
print(mytuple)
for i, x in enumerate(mytuple):
    print(i, x)
if 2 in mytuple:
    print("there is a 2 in mytuple")
mytuple2 = ("another_one",)
print(type(mytuple2))
print(mytuple.count(2))
print(mytuple.index(2))