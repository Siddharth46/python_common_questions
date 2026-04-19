#selection Sort implementation
list1 = [3,5,8,15,8,12,1]

for i in range(len(list1)):
    min_idx = i
    for j in range(i,len(list1)):
        if list1[j] < list1[min_idx]:
            min_idx = j

    list1[min_idx],list1[i] = list1[i],list1[min_idx]

        
print(list1)