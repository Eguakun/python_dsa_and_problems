# Time complexity: O(n)
# Space complexity: O(n)

def sunsetViews(buildings, direction):
    buildingsWithSunsetViews = []

    # want to loop in reverse direction that buildings are facing
    startIdx = 0 if direction == "WEST" else len(buildings) - 1
    step = 1 if direction == "WEST" else -1

    idx = startIdx
    runningMaxHeight = 0
    while idx >= 0 and idx < len(buildings):
        buildingHeight = buildings[idx]

        # compare to running max height and make decision based on greater than lesss than
        if buildingHeight > runningMaxHeight:
            buildingsWithSunsetViews.append(idx)

        runningMaxHeight = max(runningMaxHeight, buildingHeight)
        idx += step

    if direction == "EAST":
        return buildingsWithSunsetViews[::-1]
    return buildingsWithSunsetViews