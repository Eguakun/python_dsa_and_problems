
# Time complexity: O(br)
# Space complexity: O(br)
def apartment_hunting(blocks, reqs):
    minDistanceFromBlocks = list(map(lambda req: getMinDistances(blocks, req),reqs))
    # min distances of all the blocks is a map of all the requirements where for each requiremtn we get all the
    # min distanes of that reuqiremtn of every single block

    # now we have the min distances, now we want to find the maximum distances at each block given all the minimum distances at each block

    maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistanceFromBlocks)
    return getIdxAtMinValue(maxDistancesAtBlocks)

# O(b) time method
def getMinDistances(blocks, req):
    minDistances = [0 for block in blocks]
    closestReqIdx = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            # closest of that requirement in this direction right to left
            closestReqIdx = i
        minDistances[i] = distanceBetween(i, closestReqIdx)
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            # closest of that requirement in this direction left to right
            closestReqIdx = i
        minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))
    return minDistances

#O(1)
def distanceBetween(a, b):
    return abs(a - b)

def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
    maxDistancesAtBlocks = [0 for block in blocks]
    for i in range(len(blocks)):
        minDistancesAtBlock = list(map(lambda distances: distances[i],minDistancesFromBlocks))
        maxDistancesAtBlocks[i] = max(minDistancesAtBlock)
    return maxDistancesAtBlocks

def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue