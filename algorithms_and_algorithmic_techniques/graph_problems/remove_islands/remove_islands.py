# algorithmic recap - solution 1:
# 1 - we started by creating an aux data strcutre that could tell us which positions are connected to the border
# - 1a this aux data structure was completely filled with falses and was the exact same height and width as our input matrix
# - then we looped through all of the borders of our original input matrix and found all of the ones that were connected to this border
# we did this by performing a depth first search on all of the ones that were connected to the border
# this dfs looked for any horizaontally or vertically adjacent ones that we have not marked as connected to the border
# if we had already marked them, we skip them because they are connected to the border and are not islands.
# marked 1s as true that were connected to the border
# looped through interior of our matrix and for every single position we found a 1,
# we replaced it with a 0 if it didn't have a value of true in the aux data structure

# runs in O(W * H) , where w is width and h is height, b/c we could look at every position in the input matrix

# O(wh) time | O(wh) space
# Solution 1
def removeIslands(matrix):
    # define our auxiliary data structure
    onesConnectedToBorder = [[False for col in matrix[0]] for row in matrix]

    # loop through all positions in our input matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # check if the current position is equal to a border
            rowIsBorder = row == 0 or row == len(matrix) - 1
            colIsBorder = col == 0 or col == len(matrix[row] - 1)
            isBorder = rowIsBorder or colIsBorder
            if not isBorder:
                continue

            # check if position is equal to one
            if matrix[row][col] != 1:
                continue
            # if position is equal to one, perform dfs, take in matrix and position, and modify onesCoonected and
            # set them equal to true in aux data structure
            findOnesConnectedToBorder(matrix, row, col, onesConnectedToBorder)

# check if ones connected to border at current position is equal to true
    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            if onesConnectedToBorder[row][col]:
                continue
            matrix[row][col] = 0 # if not we set it equal to 0
    return matrix # finish algorithm by returning input matrix

def findOnesConnectedToBorder(matrix, startRow, startCol, onesConnectedToBorder):
    stack = [(startRow, startCol)]

    while len(stack) > 0:
        currentPosition = stack.pop()
        currentRow, currentCol = currentPosition

        alreadyVisited = onesConnectedToBorder[currentRow][currentCol]

        if alreadyVisited:
            continue

        onesConnectedToBorder[currentRow][currentCol] = True

        neighbors = getNeighbors(matrix, currentRow, currentCol)
        for neighbor in neighbors:
            row, col = neighbor

            if matrix[row][col] != 1:
                continue

            stack.append(neighbor)

def getNeighbors(matrix, row, col):
    neighbors = []

    numRows = len(matrix)
    numCols = len(matrix[row])

    if row - 1 >= 0: # UP
        neighbors.append((row - 1, col))
    if row + 1 < numRows: # DOWN
        neighbors.append((row + 1, col))
    if col - 1 >= 0: # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < numCols: # RIGHT
        neighbors.append((row, col + 1))

    return neighbors


