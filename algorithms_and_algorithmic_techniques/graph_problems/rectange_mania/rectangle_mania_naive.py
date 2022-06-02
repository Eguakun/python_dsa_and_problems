# Time complexity of naive solution: O(n ^2)
# Space complexity:O(n ^ 2) where n is the number of coordinates

def rectangleMania(coords):
    coordsTable = getCoordsTable(coords)
    return getRectangleCount(coords, coordsTable)

def getCoordsTable(coords):
    coordsTable = dict()
    # to get the coords table, we run a double for loop through all the coordinates and
    for coord1 in coords:
        coord1Directions = {
            UP: [],
            RIGHT: [],
            DOWN: [],
            LEFT: [],
        }
        for coord2 in coords:
            # we say whats the direction of this coordinate with respect to the first one
            coord2Direction = getCoordDirection(coord1, coord2)
            if coord2Direction in coord1Directions:
                coord1Directions[coord2Direction].append(coord2)
        coord1String = coordToString(coord1)
        coordsTable[coord1String] = coord1Directions
    return coordsTable

# establish coordinate direction based on checks and if it is we store it in the coord directions
# we do this for every coordinate and store it all in the hash table: coordsTable and return the table
def getCoordDirection(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    if y2 == y1:
        if x2 > x1:
            return RIGHT
        elif x2 < x1:
            return LEFT
    elif x2 == x1:
        if y2 > y1:
            return UP
        elif y2 > y1:
            return DOWN
    return ''

def getRectangleCount(coords, coordsTable):
    rectangleCount = 0
    for coord in coords:
        rectangleCount += clockwiseCountRectangles(coord, coordsTable, UP, coord)
    return rectangleCount

def clockwiseCountRectangles(coord, coordsTable, direction, origin):
    coordString = coordToString(coord)
    if direction == LEFT:
        rectangleFound = origin in coordsTable[coordString][LEFT]
        return 1 if rectangleFound else 0
    else:
        rectangleCount = 0
        nextDirection = getNextClockwiseDirection(direction)
        for nextCoord in coordsTable[coordString][direction]:
            rectangleCount += clockwiseCountRectangles(nextCoord, coordsTable, nextDirection, origin)
        return rectangleCount

def getNextClockwiseDirection(direction):
    if direction == UP:
        return RIGHT
    if direction == RIGHT:
        return DOWN
    if direction == DOWN:
        return LEFT
    return ''


def coordToString(coord):
    x, y = coord
    return str(x) + '-' + str(y)



UP = 'up'
RIGHT = 'right'
DOWN = 'down'
LEFT = 'left'
