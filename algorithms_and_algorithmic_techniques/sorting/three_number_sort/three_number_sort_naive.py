# O(n) time complexity , n is the length of the array
# O(1) space complexity
def threeNumberSort(array, order):
    valueCounts = [0, 0, 0]

    # start by counting the unique values from our order array and store that in value counts
    for element in array:
        orderIdx = order.index(element)
        valueCounts[orderIdx] += 1

    # then we loop through all of these value counts
    for i in range(3):
        # get the value
        value = order[i]

        # get the count
        count = valueCounts[i]

        # update the array at the according indices
        numElementsBefore = sum(valueCounts[:i])

        for n in range(count):
            currentIdx = numElementsBefore + n
            array[currentIdx] = value

    return array

