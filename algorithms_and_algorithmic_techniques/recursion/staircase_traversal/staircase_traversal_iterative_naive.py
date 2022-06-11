# Time Complexity: O(n * k)
# Space Complexity: O(n)
def staircaseTraversal(height, maxSteps):
    waysToTop = [0 for _ in range(height + 1)]  # indices in this data strcture represent number of wyas to get to top or a stiarcase of that index height
    waysToTop[0] = 1
    waysToTop[1] = 1

    for currentHeight in range(2, height + 1):  # loop through
        step = 1
        while step <= maxSteps and step <= currentHeight:  # k work -> condition is for making sure were not overextendig and doing too many calculations
            # looks back in our data structre and check firs and second step behind and add that to current result
            waysToTop[currentHeight] = waysToTop[currentHeight] + waysToTop[currentHeight - step]
            step += 1
    return waysToTop[height]