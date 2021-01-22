"""
This is a pratice file for Set
A Set is a unordered and unindexed collection of objects
"""
myset = {0, "one", 2, "three", 4}
print(type(myset), "size: ",len(myset))
print(myset)
print("dfd" in myset)
myset.add("five")
print(myset)
myset.update({6, "seven"})
print(myset)
myset.remove(6)
myset.discard(6)
print(myset)