# could cycle through the array and for every integer, locate the integer that is located at the jump spot.
# pop the value that is located at the jump spot from the array, and repeat the same step for the remaining values
# in the array. At the end if the array is empty, then return True, else return False

# Time complexity O(n) n is the length of the input array
# Space complexity: O(1)



# jump through the elements in the array, visiting exactly n elements, where n is the length of the array.
# at any point if after the first element that we start at, we find ourselves back at the first index, then we know that we found multiple cycles and similarly
# once we jump through 6 elements if were not at the starting index then we know we have multiple cycles

def hasSingleCycle(array):
    numElementsVisited = 0
    currentIdx = 0 # starting index
    while numElementsVisited < len(array):
        if numElementsVisited > 0 and currentIdx == 0:
            return False
        numElementsVisited += 1

        currentIdx = getNextIdx(currentIdx, array)
    # once we visited 6 elements, then we have to be back at the starting index,
    return currentIdx == 0

def getNextIdx(currentIdx, array):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array) # loop around, for numbers that spill outside bounds of array
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)  # if youre dealing with a negative number, you need to adjust for that
    # if we had to deal with decimals, we could floor it.

