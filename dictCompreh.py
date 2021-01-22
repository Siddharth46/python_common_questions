"""this is a program to practice comprehension
Comprehension in python provides us with a short 
and concise way to construct new sequence such as
list, Set, dict etc using sequence which is already 
defined"""

#output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}

dict1 = {1: "one", 2:"two", 3:"three"}
print(dict1)

dict2 = {key:key**2 for key, value in dict1.items()}
print(dict2)

list1 = [2,3,4,5]
list2 = [4,9,16,25]

dict3 = {key:value for (key,value) in zip(list1,list2)}
print(dict3)

dict4 = {key:key**3 for key in list1}
print(dict4)