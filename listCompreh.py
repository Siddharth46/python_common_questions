"""this is a program to practice comprehension
Comprehension in python provides us with a short 
and concise way to construct new sequence such as
list, Set, dict etc using sequence which is already 
defined"""

#output_list = [output_exp for var in input_list if (var satisfies this condition)]

lista = ["name", "place", "thing"]
print(lista)
print(len(lista[0]))

listb = [var for var in lista if (len(var))>4]
print(listb)

list1 = ["siddharth", "selena", "komal", "jimmy"]
print(list1)

list2 = ["".join(set(var)) for var in list1]
print(list2)

list3 = [var**2 for var in range(1,6)]
print(list3)

#Find Unique data in list and make a new list of it using comprehension

list4 = ["sid.dixit1995@gmail.com","someone@yahoo.com","someother@gmail.com","firefox@hotmail.com"]

print(list4[0].count("i"))

list5 = [(var.replace('.','@')).split('@')[-2] for var in list4]
print(list5)

list6 = ["".join(set(var.split('@')[0])) for var in list4]
print(list6)