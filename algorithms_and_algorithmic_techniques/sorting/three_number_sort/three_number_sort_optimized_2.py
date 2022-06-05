def threeNumberSort(array, order):
    firstValue = order[0]
    secondValue = order[1]

    # keep track of the indices where the values are stored
    firstIdx, secondIdx, thirdIdx = 0, 0, len(array) - 1

    # loop until second index is greater than third index
    while secondIdx <= thirdIdx:
        value = array[secondIdx]

        # check to see if second value is equal to our first value, if it is we swap them and increment the pointers
        if value == firstValue:
            array[secondIdx], array[firstIdx] = array[firstIdx], array[secondIdx]
            firstIdx += 1
            secondIdx += 1

        elif value == secondValue:
            secondIdx += 1

        else:
            array[secondIdx], array[thirdIdx] = array[thirdIdx], array[secondIdx]
            thirdIdx -= 1
    return array