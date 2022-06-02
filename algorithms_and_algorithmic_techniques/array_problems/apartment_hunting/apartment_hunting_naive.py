# time complexity: O(b^2 * r), because we are doing one for loop of length b, one nested for loop of length r, one other nested for loop of length b and in there
# we doing constant time complexity checks

# space complexity: O(b) space, bc we have max distance of blocks array
# naive solution:

def apartment_hunting(blocks, reqs):
    # declare this array thats going to take O(b) space and that array is going to hold at every block the
    # maximum distance that one of the bulindgs is at away from this block
    maxDistancesAtBlocks =[-float("inf") for block in blocks]

    for i in range(len(blocks)): # iterating through indices becasue were going to be iterating therough theb blcoks again and we want to calculate the distance bwteen two indices
        for req in reqs:  # iterate through requirements
            # were saying what is the distance of the closest of this requirement
            # for the gym where is the nearest gym
            closestReqDistance = float("inf") # reason why is here were looking for the closest garray so were probaly gonna use the min function and so initializing this to posiitve inf will make our code cleaner
            for j in range(len(blocks)):
                # now we say at every block lets first check if the curretn requiremnt that were checking for is located at that block
                if blocks[j][req]:
                    closestReqDistance = min(closestReqDistance, distanceBetween(i, j))

        # here we want to update the max distances at block
            maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i], closestReqDistance)

    return getIdxAtMinValue(maxDistancesAtBlocks)

def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue

def distanceBetween(a, b):
    return abs(a, b)


