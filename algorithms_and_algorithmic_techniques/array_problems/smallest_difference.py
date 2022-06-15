# Time complexity: O(n log (n) + m log(m)) where n is the length of array a and m is the length of array b
# We are sorting both arrays
# Space complexity: O(1) we are sorting the arrays in place and we arent using any auxiliary memory

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    # represent the indices that our pointers are ponting at
    idxOne = 0
    idxTwo = 0
    # is it okay to sort the arrays in place?

    smallest = float('inf')
    current = float('inf')
    smallestPair = []

    # if at any point were forced to increment our left pointer and were out of the array, then were done. Theres no point in keep exploting because we knowit will just get greater and greater
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]

        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]

        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
        return smallestPair



