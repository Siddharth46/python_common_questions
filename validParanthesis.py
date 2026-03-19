'''Given a string containing (), {}, [], determine if the brackets are closed in the correct order'''

def bracketCheck(s):
    stackL = []
    pairs = {')':'(',']':'[','}':'{'}
    result = True
    for char in s:
        if char in pairs.values():
            stackL.append(char)
        elif char in pairs:
            if not stackL or stackL.pop() != pairs[char]:
                result = False
    return result

def main():
    print('insert the string to check for brackets')
    s = input()
    print(bracketCheck(s))

if __name__ == '__main__':
    main()