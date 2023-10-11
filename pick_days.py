
def getdays(dict1):
    re_list = []
    for k,v in dict1.items():

        if v%2 == 0:
            re_list.append(k)
    return re_list


dict1 = {"Monday":1, "tuesday":2, "Wed":3, "thr":4, "Fri":5, "Sat":6, "SUn":7}
result = getdays(dict1)
print(result)

