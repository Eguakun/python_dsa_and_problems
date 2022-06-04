# to check if two elements are on teh same diagonal
# abs( x2-x1) == abs(y2-y1)
# if true: they are on the same diagonal

# big omega of (n!) time complexity as a lower bound, becasue you have roughly n! optioons of places
# to place a queen and then you have to do n work for each of those to check if tis a valid placement
# O(n) space complexity - recursive call stack


def nonAttackingQueens(n):
    columnPlacements = [0] * n
    return getNumberOfNonAttackingQueenPlacements(0, columnPlacements, n)


def getNumberOfNonAttackingQueenPlacements(row, columnPlacements, boardSize):
    if row == boardSize:
        return 1

    validPlacements = 0
    for col in range(boardSize):
        if isNonAttackingPlacements(row, col, columnPlacements):
            columnPlacements[row] = col
            validPlacements += getNumberOfNonAttackingQueenPlacements(row + 1, columnPlacements, boardSize)
    return validPlacements


def isNonAttackingPlacements(row, col, columnPlacements):
    for previousRow in range(row):
        columnToCheck = columnPlacements[previousRow]
        sameColumn = columnToCheck == col
        onDiagonal = abs(columnToCheck - col) == row - previousRow
        if sameColumn or onDiagonal:
            return False
    return True


