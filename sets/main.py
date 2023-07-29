# set does not allow duplicate
#myset = {1,2,3,1,2}

#print(myset)

#myset = set([1,2,3,2])

myset1 = set(["Hello","Nguyen","Hello"])

# list is immutable, set is mutable
#print(myset)

myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

#myset.remove(3)
#myset.discard(2)
for i in myset:
    print(i)

if 2 in myset:
    print("Yes")

# Union

