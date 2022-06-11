# Time Complexity: O(n * k)
# Space Complexity: O(n)
def staircaseTraversal(height, maxSteps):
    return numberOfWaysToTop(height, maxSteps, {0: 1, 1: 1})


def numberOfWaysToTop(height, maxSteps, memoize):
    # implementing our base case
    if height in memoize:
        return memoize[height]

    numberOfWays = 0
    # try all of the possible steps to figure out what those values are
    for step in range(1, min(maxSteps, height) + 1):
        numberOfWays += numberOfWaysToTop(height - step, maxSteps)
    memoize[height] = numberOfWays
    return numberOfWays


