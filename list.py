"""
This is the practice programe for List
A list is an ordered and changable collection of objects
"""
mylist = []
mylist.append(2)
mylist.extend([4, 5, 6])
mylist[0] = 3
print(len(mylist))
print(mylist)
for i, x in enumerate(mylist):
    print(i, x)
print("the 1:3 slice in list is:",mylist[1:3])
mylist2 = list(mylist)
mylist1 = [7,8,9]
mylist.pop()
print(mylist)
del mylist[0]
print(mylist)
mylist.clear()
print(mylist)
print("mylist2:",mylist2)
mylist3 = ["x"]*10
mylist4 = ["y"]*10
newlist = mylist3 + mylist4
print(set(newlist))