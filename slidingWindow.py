#program to find longest substring without repeating characters using sliding window technique
def longest_substring(s):
    
    sett = set()
    left = 0
    longest_substring=''
    for r in range(len(s)):
        while s[r] in sett:
            sett.remove(s[left])
            left += 1

        sett.add(s[r])

        if len(s[left:r+1])> len(longest_substring):
            longest_substring = s[left:r+1]
        

    return longest_substring

def main():
    s = input( 'Insert string to find longest substring of. ')
    result = longest_substring(s)
    print('Longest substring without repeating characters is: ', result)

if __name__ == '__main__':
    main()