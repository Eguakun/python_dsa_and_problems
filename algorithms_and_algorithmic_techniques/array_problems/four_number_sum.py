# Time complexity: O(n ^ 2) - avg one for loop where we iterate through all and inside that one were doing two other for loops one tht iteratest hroguh the number after and numbers before our curreent umber
#each oft hsoe pairs takes o(n^2) time and if you add them its 2n drop the constants

# in the inner for loops for the most part its ocnstant but the the one that iterates all the numbers after our current number,
# check if theres a correspodning pair that sums up to the diffrence of 16 and our current number we create all our quadruplets.
# we have to iterate through all the pairs, there could be a worst case where you have a vunch of pairs O(N^3)

# Space complexity: O(N^2) avg O(N^3) worst - hashtable of quadruplets

def fourNumberSum(array, targetSum):
    allPairSums = {}
    quadruplets = []

    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[i] + array[j]])
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])
    return quadruplets


