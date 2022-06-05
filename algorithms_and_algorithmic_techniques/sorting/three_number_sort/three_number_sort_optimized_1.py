# O(n) time
# O(1) space

def threeNumberSort(array, order):
    # defining first value and third value of our ordering
    firstValue = order[0]
    thirdValue = order[2]

    firstIdx = 0
    # looking for all the elements that have the same value as our first value and pushing them to the beginning of the array
    for idx in range(len(array)):
        if array[idx] == firstValue:
            array[firstIdx], array[idx] = array[idx], array[firstIdx]
            firstIdx += 1

    thirdIdx = len(array) - 1
    # we go for our backwards pass where we do the same thing except we look for our third value and push all of those to the end of the array
    for idx in range(len(array) -1 , -1, -1):
        if array[idx] == thirdValue:
            array[thirdIdx], array[idx] = array[idx], array[thirdIdx]
            thirdIdx -= 1
    return array

