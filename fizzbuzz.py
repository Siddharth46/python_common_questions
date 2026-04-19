#program that print integers from 1 to n but replace divisble by 3 with Fizz divisible by 5 with Buzz and divisible with both 3 and 5 with FizzBuzz

def fizzBuzz(n):
    for num in range(1,int(n)+1):
        if num%3 == 0 and num%5==0:
            print('FizzBuzz')
        elif num%3 == 0:
            print('Fizz')
        elif num%5 == 0:
            print('Buzz')
        else:
            print(num)

def main():
    n = input('insert N (no. to count till)')
    fizzBuzz(n)

if __name__ == '__main__':
    main()