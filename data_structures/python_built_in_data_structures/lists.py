import random
#indexing

x = ['pig', 'cow', 'horse']
print(x[2])


# slicing
# [start:end+1:step]

print(x[0:2])
print(x[0:3:2])


# concatenation

m = ["I'm the ", "world's", "greatest"]
fk = ["These", " are ", "facts"]

c = m + fk
print(c)


# iterating -

# index and item
y = [7,8,3]
for index, item in enumerate(y):
    print(index, item)

j = [9,8,0,99,8,4]
j.sort(reverse=True)
print(j)


# List comprehension

# get values within a range
under_10 = [x for x in range(10)]
print('under_10: ' + str(under_10))

# get squared values
squares = [x**2 for x in under_10]
print('squares: ' + str(squares))

# get odd numbers using mod
odds = [x for x in range(10) if x % 2 == 1]
print('odds: ' + str(odds))

# get multiples of 10
ten_x = [x * 10 for x in range(10)]
print("multiples of 10: ", ten_x)

# get all numbers from a string
s = "I love 2 go to the st0re 11 tim3s per week!"
nums = [x for x in s if x.isnumeric()]
print("nums: " + "".join(nums))

# get index list of an item
names = ["oscar", "carlos", "felix", "johnny", "pedro", "ray"]
idx = [k for k, v in enumerate(names) if v == "felix"]
print('index= ' + str(idx[0]))

# delete an item from a list
letters = [x for x in 'ABCDEF']
random.shuffle(letters)
ltrs = [a for a in letters if a != 'C']
print(letters, ltrs)








