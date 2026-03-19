#revese a list without using inbuilt functions
list1 = ['one','two','three','four']

def main():
    print(f"reversing list {list1}")
    list2 = [elem for elem in list1[-1::-1] ]
    print(f'solution1: {list2}')

    i,j =0,len(list1)-1
    while i<j:
        list1[i], list1[j] = list1[j], list1[i]
        i+= 1
        j-= 1
    print(f'solution2: {list1}')

if __name__ == '__main__':
    main()