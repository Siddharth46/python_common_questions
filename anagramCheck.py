'''An anagram check asks whether two strings contain the same characters in the same quantities, just possibly in a different order.'''
from collections import Counter

def anagramCheck(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    sc1 = Counter(s1)
    sc2 = Counter(s2)
    if sc1 == sc2:
        return True
    else:
        return False
    

def main():
    s1 = input('Insert string1 ')
    s2 = input('Insert String2 ')
    result = anagramCheck(s1,s2)
    print(result)

if __name__ == '__main__':
    main()