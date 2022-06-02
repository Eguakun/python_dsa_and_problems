# key value pair
# hash map
# dictionaries are unordered
# orderedDict is a way to get an ordered dictionary. Must use python collection

# 3 different ways to create a dictionary

x1 = {"chicken": 25, "morris": 299238, "boiled nuts": 33}

x2 = dict([('chicken', 25), ('morris', 299238), ("boiled nuts", 33)])

x3 = dict(chicken=25, morris=299328, boiled_nuts=33)

# dictionary operations

# add or update
x1['chicken'] = 99

# delete an item
del(x1['chicken'])

# get length of dict x1
len(x1)

# delete all items from dict x1
x1.clear()

# delete dict x1
del(x1)


# accessing keys and values in a dictionary
print(x2.keys())
print(x2.values())
print(x2.items())

# check membership in x2_keys --> only looks in keys, not values
print("chicken" in x2)

# check membership in x2 values
print(32 in x2.values())


# iterating a dictionary --> items are in random order
# you cant iterate these in a sorted order
for key in x2:
    print(key, x2[key])

for k, v in x2.items():
    print(k,v)