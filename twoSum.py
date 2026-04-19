'''Given an array of numbers and a target sum, find two distinct numbers in 
the array whose values add up to the target.'''

numList = [2,7,11,12]
target = 9

print(f'for list {numList} where target is {target}')

seen={}
for i, j in enumerate(numList):
    need = target - j
    if need in seen:
        print(i,seen[need])
    seen[j] = i

'''for i in range(len(numList)-1):
    for j in range(1,len(numList)-1):
        if numList[i] + numList[j] == target:
            print(f'{numList[i],numList[j]}')
            break'''