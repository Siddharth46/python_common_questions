
import sys
def check_palindrome(input_string):
    reverse_input = str(input_string)[::-1]
    if reverse_input == str(input_string):
        return True
    return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("please input a string in arg with the script!")
    else:
        input_string = sys.argv[1]
        result = check_palindrome(input_string)
        print(f"palindrome: {result}")