'''function to count unique elements in string'''

def count_unique(input_string):
    unique_elem = set(char for char in input_string.lower() if char.isalpha())
    print(unique_elem)
    result = {}
    for elements in unique_elem:
        occurances = input_string.lower().count(elements)
        result[elements] = occurances
    return result


response = count_unique("lDsr Dkj asdf fe")
print(response)