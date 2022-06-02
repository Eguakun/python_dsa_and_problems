# Time complexity: O(n ^ 2)
# Space complexity: O(n)

def rectangleMania(coords):
    coordsTable = getCoordsTable(coords)
    return getRectangleCount(coords, coordsTable)

def getCoordsTable(coords):
    coordsTable = {"x": {}, "y": {}}
    for coord in coords:
        x, y = coord
        if x not in coordsTable["x"]:
            coordsTable["x"][x] = []
        coordsTable["x"][x].append(coord)
        if y not in coordsTable["y"]:
            coordsTable["y"][y] = []
        coordsTable["y"][y].append(coord)
    return coordsTable


def getRectangleCount():
    pass