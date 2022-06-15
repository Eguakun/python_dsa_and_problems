# when we look at the matrix we realize te only thing we care about is positive
# once we have positives we can flip the adjacents but we have to find positive first
# once we find firs one we know the next numbers that will be positive since we have to flip them
# were going to use a queue,
# we will have one queue and it is going to store all positions of elements that are positive
# that way we cna pop them off queue, look at lal their neighbors and turn any neighbors form negative to positive
# then we can take all values that we converted and add them another data structure
# to keep track that we switched them to be positive

# now lets use these for the next pass

# once there are no negatives we can return
# if we can't make switches return -1


# Time O(w *h) because we do w * h at the beginning of the operation by looking through elements and add all positive values of queue
# Space O(w * h)

# entry point
def minimumPassesOfMatrix(matrix):
    # number of passes
    passes = convertNegatives(matrix)
    # if we dont contain any negatives
    return passes - 1 if not containsNegative(matrix) else -1


def convertNegatives(matrix):
    # gives us a queue of all positive positions
    nextPassQueue = getAllPositivePositions(matrix)
    passes = 0

    while len(nextPassQueue) > 0:
        # if not empty we swap the queues
        currentPassQueue = nextPassQueue
        nextPassQueue = []

        # loop through current pass queue pop
        while len(currentPassQueue) > 0:
            currentRow, currentCol = currentPassQueue.pop(0)
            adjacentPositions = getAdjacentPositions(currentRow, currentCol, matrix)
            for position in adjacentPositions:
                row, col = position
                value = matrix[row][col]
                # if negative switch to positive
                if value < 0:
                    matrix[row][col] = value *-1
                    nextPassQueue.append([row, col])
                    # continue until there are no more elements
        passes += 1
    return passes

def containsNegative(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True


def getAllPositivePositions(matrix):
    positivePositions = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            value = matrix[row][col]
            if value > 0:
                positivePositions.append([row,col])
    return positivePositions


def getAdjacentPositions(row, col, matrix):
    adjacentPositions = []

    if row > 0:
        adjacentPositions.append([row -1, col])

    if row < len(matrix) - 1:
        adjacentPositions.append([row + 1, col])

    if col > 0:
        adjacentPositions.append([row, col - 1])

    if col < len(matrix[0]) - 1:
        adjacentPositions.append([row, col + 1])

    return adjacentPositions


