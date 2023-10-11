def factorials(number):
    if number == 0 or number == 1:
        return 1
    return number * factorials(number-1)
result = factorials(5)
print(result)