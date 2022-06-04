# time complexity: O(n ^ 2)
# space complexity: O(1)

def firstDuplicateValue(array):
    minimumSecondIndex = len(array)
    for i in range(len(array)):
        value = array[i]
        for j in range(i + 1, len(array)):
            valueToCompare = array[j]
            if value == valueToCompare:
                minimumSecondIndex = min(minimumSecondIndex, j)
    if minimumSecondIndex == len(array):
        return -1

    return array[minimumSecondIndex]