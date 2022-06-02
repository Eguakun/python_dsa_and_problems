# Immutable (can't change or add data once tuple is created)
# Useful for fixed data
# Faster than lists
# sequence type

# indexing

tu = ('Morris', 'Chan', 'Oscar', 'Kim')

print(tu[2])

# slicing
# [start:end+1:step]

print(tu[0:2])
print(tu[0:3:2])


tu2 =("Morris", " Evan ")
tu3 = ("Eguakun ", "will succeed!")

tu4 = tu2 + tu3
print(tu4)

# tuples are immutable but member objects may be mutable.
# if you have a list as a member of a tuple, you can change the values in the list within the tuple

# you can also concatenate two tuples


y = ([1, 2], 3)
y += (4,)
print(y)

