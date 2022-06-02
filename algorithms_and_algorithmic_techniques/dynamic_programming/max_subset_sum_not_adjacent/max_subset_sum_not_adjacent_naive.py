# formula for algorithm
# maxSums[2] = max(maxSums[1], maxSums[0] + array[2])
# maxSums[i] = max(maxSums[i - 1, maxSums[i - 2] + array[i])
# Time complexity: O(n), where n is the length of our input array
# Space complexity: O(n)

def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])
    return maxSums[-1]




