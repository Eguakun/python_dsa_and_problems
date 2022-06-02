# Store non duplicate items
# Very fast access vs. Lists
# Great for checking membership
# Math set ops (union, intersect)
# Sets are unordered

x = {3,5,6,5,33}

# print(x)

# add to a set
x.add(7)

# remove from a set
x.remove(3)

# get length of a set x
len(x)

# check membership of a set x
# print(5 in x)

# pop random item from a set x
# print(x.pop(), x)

# delete all items from a set x
x.clear()

# Mathematical set operations

s1 = {1, 2, 3}
s2 = {3, 4, 5}

# intersection (AND): set1 & set2
print(s1 & s2)

# union (OR): set1 | set2
print(s1 | s2)

# symmetric difference/ exclusive or (XOR): set1 ^ set2 , either in s1 or in s2 but not in both
print(s1 ^ s2)

# difference (in set 1 but not in set 2): set1 - set2
print(s1 - s2)

# subset (set2 contains set1): set1 <= set2
print(s1 <= s2)

# superset (set1 contains set2): set1 >= set2
print(s1 >= s2)

