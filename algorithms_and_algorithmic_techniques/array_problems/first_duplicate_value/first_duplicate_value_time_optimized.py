# algorithm instructions

# Create a set
# iterate through the array
# for each value check if the value is in the seen set
# if the value is not in the seen set, add it to the seen set

# once you add the first value to the seen set, move on to the next value
# check to see if the next value is in the seen set

# if it is, return that value.

# if it is not, add that value to the seen set and move on to the next value

# time complexity: O(n)
# space complexity: O(n)

def firstDuplicateValue(array):
    seen = set()
    for value in array:
        if value in seen:
            return value
        seen.add(value)

    return -1
