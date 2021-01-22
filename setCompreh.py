"""this is a program to practice comprehension
Comprehension in python provides us with a short 
and concise way to construct new sequence such as
list, Set, dict etc using sequence which is already 
defined"""

#Set comprehensions are pretty similar to list comprehensions.
#The only difference between them is that set comprehensions use curly brackets { }

list1 = [2,3,4,5]
print(list1)

set1 = {var**2 for var in list1}
print(set1)

set2 = {var+2 for var in set1}
print(set2)