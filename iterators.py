list1 = [2,3,4,5]

myiter = iter(list1)
print(type(myiter))
while True:
    try:
        print(next(myiter))
    except StopIteration:
        print("stopIteration")
        with open("new.txt","a") as f:
            f.write("StopIteration")
        break
