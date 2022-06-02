# Time complexity: O(log(n)) - length of the array
# Space complexity: Recursive implementation: OL(log(n)) becasue of frames used on call stack with all calls
# Iterative implementation has O(1) space complexity and O(log(n)) time complexty

# Recursive Implementation

def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

def shiftedBinarySearchHelper(array, target, left, right):
    # Recursive base case - what happens when left pointer exceeds right pointer
    if left > right:
        return - 1
    middle = (left + right) // 2
    potentialMatch = array[middle]
    leftNum = array[left]
    rightNum = array[right]

    if target == potentialMatch:
        return middle
    elif leftNum <= potentialMatch: # left half is sorted
        if target < potentialMatch and target >= leftNum:
            return shiftedBinarySearchHelper(array, target, left, middle - 1) # explore only left half
        else:
            return shiftedBinarySearchHelper(array, target, middle + 1, right) # explore only right half
    else: # right section was in sorted order but not left
        if target > potentialMatch and target <= rightNum:
            shiftedBinarySearchHelper(array, target, middle + 1, right)
        else: # target is less than potential match or greater than right num, explore left half
            return shiftedBinarySearchHelper(array, target, left, middle - 1)



# Iterative implementation:

def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

def shiftedBinarySearchHelper(array, target, left, right):
    while left <= right:

        middle = (left + right) // 2
        potentialMatch = array[middle]
        leftNum = array[left]
        rightNum = array[right]

        if target == potentialMatch:
            return middle
        elif leftNum <= potentialMatch: # left half is sorted
            if target < potentialMatch and target >= leftNum:
                right = middle - 1 # explore only left half
            else:
                left = middle + 1 # explore only right half
        else: # right section was in sorted order but not left
            if target > potentialMatch and target <= rightNum:
                left = middle + 1
            else: # target is less than potential match or greater than right num, explore left half
                right = middle - 1
    return -1



