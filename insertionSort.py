#insertion sort implementation

l1 = [2,6,5,0,3,8]

for i in range(1,len(l1)):
    key = l1[i]
    j = i-1
    while j >= 0 and key < l1[j]:
        l1[j+1] = l1[j]
        j = j-1
    l1[j + 1] = key
print(l1)
