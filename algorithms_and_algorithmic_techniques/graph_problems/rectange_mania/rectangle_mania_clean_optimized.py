# we dont need to do the clockwise traversal of points
# if we have ,while being sure to take into account the principle of
# treating every coordinate as potential bottom left corner
# if we have potential bottom left corner, we know that if this is going to be a real rectangle,
# there must be a corresponding top right corner, meaning a corner opposite our corner.
# any point in the upper right vicinity of our point is a valid right corner
# in order to validate as rectangels, all we need to do is find top left and btoom right corners, and we can do that
# because we already have all teh coordinates
# if i map and store the coordinates ina hash table for fast lookup then
# i cna iterate through all the coordingtes, treat every cooridnate as potential bottom left corners
# then do a double for loop and iterate through all the other coordinates again
# and treat every coordinate thats in the upper right and see if top left is in our hash table
# and see if bottom right is in the hash table
# if both are there, then count the rectangle

# Time Complexity: O(n ^ 2)
# Space complexity: O(n)

def rectangleMania(coords):
    coordsTable = getCoordsTable(coords)
    return getRectangleCount(coords, coordsTable)

def getCoordsTable(coords):
    coordsTable = {}
    for coord in coords:
        coordString = coordToString(coord)
        coordsTable[coordString] = True
    return coordsTable

def getRectangleCount(coords, coordsTable):
    rectangleCount = 0
    for x1, y1 in coords:
        for x2, y2 in coords:
            if not isInUpperRight([x1, y1], [x2, y2]):
                continue
            upperCoordString = coordToString([x1,y2])
            rightCoordString = coordToString([x2, y1])
            if upperCoordString in coordsTable and rightCoordString in coordsTable:
                rectangleCount += 1
    return rectangleCount


def isInUpperRight(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return x2 > x1 and y2 > y1



def coordToString(coord):
    x, y = coord
    return str(x) + '-' + str(y)