'''this program is to check if a given string is pangram'''
import sys

def check_pangram(sentence):
    unique_alphabets = set(char for char in sentence.lower() if char.isalpha())
    print(unique_alphabets)
    if len(unique_alphabets) == 26:
        return True
    return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("please input a string in arg with the script!")
    else:
        sentence = sys.argv[1]
        result = check_pangram(sentence)
        print(f"pangram: {result}")
