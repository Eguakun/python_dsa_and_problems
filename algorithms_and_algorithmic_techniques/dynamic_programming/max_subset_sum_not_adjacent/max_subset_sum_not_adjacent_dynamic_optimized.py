# we never look at max sums of i -3
# we only need two stored values at any given point in time
# we dont need the entire array
# store just the two values

# first = maxSums[i - 1]
# second = maxSums[i - 2]
# at any time were iterating through our main array and we want to build max sums of i

# current_greatest_sum =  max(first, second + array[i])

# at the end of each iteration, we have to update first and second:
# first = current_greatest_sum
# second = first

# Time complexity: O(n)
# Space complexity: O(1)

# Potential edge cases: what if we have negative integers? Have to change formula
# Do we want to keep track of numbers that make up the sum?
# can the array hold values other than integers, such as strings?
# - what do we do in this case?

def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    second = array[0]
    # if theres an edge case of needing to keep track of the numbers:
    # - second = [array[0], [0]]
    # - append this array of indices whose numbers are used to keep trck of the sum
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first

