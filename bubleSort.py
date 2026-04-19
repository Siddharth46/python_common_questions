#sory array using buble sorts

list1 = [42, 7, 19, 2, 88, 33, 17, 100, 0, 55]
for j in range(len(list1)):
    for i in range(len(list1)-1-j):
        if list1[i] > list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]

print(list1)