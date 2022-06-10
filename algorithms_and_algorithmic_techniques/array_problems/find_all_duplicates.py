from collections import Counter
def findAllDuplicates(array):


    c = Counter(array)
    res = []

    for k,v in c.items():
        if v > 1:
            res.append(k)
    return res

a = [1,1,1,2,3,3,3,4,5,5,6,7,7]
# should return 1, 3, 5, 7
print(findAllDuplicates(a))