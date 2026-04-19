#find duplicate in given array
from collections import Counter

def find_duplicate():
    arr = [1, 2, 3, 2, 4,5, 2, 1]
    duplicates = [i for i in set(arr) if arr.count(i)>1]
    print(duplicates)

    print('Solution 2')
    seen = set()
    dupl = set()
    for elem in arr:
        if elem in seen:
            dupl.add(elem)
        else:
            seen.add(elem)
    print(dupl)

    print('solution3: ')
    dupl2 = []
    arrCount = dict(Counter(arr))
    for elem in arrCount:
        if arrCount[elem] > 1:
            dupl2.append(elem)
    print(dupl2)


if __name__ == '__main__':
    find_duplicate()