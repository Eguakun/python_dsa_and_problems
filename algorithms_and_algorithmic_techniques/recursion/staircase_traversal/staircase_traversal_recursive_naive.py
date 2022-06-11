# Time Complexity: O(k^n)
# Space Complexity: O(n)
def staircaseTraversal(height, maxSteps):
    return numberOfWaysToTop(height, maxSteps)

def numberOfWaysToTop(height, maxSteps):
    # implementing our base case
    if height <= 1:
        return 1

    numberOfWays = 0
    # try all of the possible steps to figure out what those values are
    for step in range(1, min(maxSteps, height) + 1):
        numberOfWays += numberOfWaysToTop(height - step, maxSteps)

    return numberOfWays


