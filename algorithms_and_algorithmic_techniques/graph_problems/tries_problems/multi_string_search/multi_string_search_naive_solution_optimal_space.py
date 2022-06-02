# Space Complexity: O(n) where n is the length of the list of small strings

# Time Complexity: O(n * b * s)
# n - number of small strings we have ,
# b - length of big string,
# s - length of biggest small string

# for every character in the big string, were doing at most s other iterations




# suffix tree solution time and space complexity:

# building the suffix tree will take O(b ^2) time
# space = O(b^2)

# Time O(b^2 + ns)
# Space O(b^2 + n)

# b^2 for building the suffix tree and ns for checking for the string



# First naive solution: ITerate through small strigns and checking if they are in big string by comparing al characters
# Time: O(bns) | space: O(n) 
def naiveMultiStringSearch(bigString, smallStrings):
    return [isInBigString(bigString, smallString) for smallString in smallStrings]

def isInBigString(bigString, smallString):
    for i in range(len(bigString)):
        # if we get to the point where the length of the small string is too big, given the index i that were
        # at in the big string, we migh as well just end it and break at that point
        if i + len(smallString) > len(bigString):
            break
        if isInBigStringHelper(bigString, smallString, i):
            return True
    return False

def isInBigStringHelper(bigString, smallString, startIdx):
    leftBigIdx = startIdx
    rightBigIdx = startIdx + len(smallString) - 1
    leftSmallIdx = 0
    rightSmallIdx = len(smallString) - 1
    while leftBigIdx <= rightBigIdx:
        if(
            bigString[leftBigIdx] != smallString[leftSmallIdx] or
            bigString[rightBigIdx] != smallString[rightSmallIdx]
        ):
            return False
        leftBigIdx += 1
        rightBigIdx -= 1
        leftSmallIdx += 1
        rightSmallIdx -= 1

    return True



