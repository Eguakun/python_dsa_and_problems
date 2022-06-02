# Solution 2 - No extra auxiliary data structure, which allows for a better average space complexity but it is the same for worst case
# O(wh) time | O(wh) space - still using stack that could have at most wh elements inside of it
def removeIslands(matrix):

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
            changeOnesConnectedToBorderToTwos(matrix, row, col)

# check if ones connected to border at current position is equal to true
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            color = matrix[row][col]
            if color == 1:
                matrix[row][col] = 0
            elif color == 2:
                matrix[row][col] = 1

    return matrix # finish algorithm by returning input matrix

def changeOnesConnectedToBorderToTwos(matrix, startRow, startCol):
    stack = [(startRow, startCol)]

    while len(stack) > 0:
        currentPosition = stack.pop()
        currentRow, currentCol = currentPosition

        matrix[currentRow][currentCol] = 2

        neighbors = getNeighbors(matrix, currentRow, currentCol)
        for neighbor in neighbors:
            row, col, = neighbor

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

