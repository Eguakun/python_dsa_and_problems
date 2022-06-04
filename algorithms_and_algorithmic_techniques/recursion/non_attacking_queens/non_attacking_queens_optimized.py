# to check if two elements are on teh same diagonal
# abs( x2-x1) == abs(y2-y1)
# if true: they are on the same diagonal

# O(n!) time complexity , becasue you have roughly n! optioons of places to place a queen
# to place a queen and then you have to do n work for each of those to check if tis a valid placement
# O(n) space complexity - recursive call stack


def nonAttackingQueens(n):
    blockedColumns = set()
    blockedUpDiagonals = set()
    blockedDownDiagonals = set()

    return getNumberOfNonAttackingQueenPlacements(0, blockedColumns,blockedUpDiagonals,blockedDownDiagonals, n)


def getNumberOfNonAttackingQueenPlacements(row, blockedColumns, blockedUpDiagonals, blockedDownDiagonals,  boardSize):
    if row == boardSize:
        return 1

    validPlacements = 0
    for col in range(boardSize):
        if isNonAttackingPlacements(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
            placeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals)
            validPlacements += getNumberOfNonAttackingQueenPlacements(row + 1, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, boardSize)
            removeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals)
    return validPlacements


def placeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
    blockedColumns.add(col)
    blockedUpDiagonals.add(row + col)
    blockedDownDiagonals.add(row - col)

def removeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
    blockedColumns.remove(col)
    blockedUpDiagonals.remove(row + col)
    blockedDownDiagonals.remove(row - col)

def isNonAttackingPlacements(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
    if col in blockedColumns:
        return False
    if row + col in blockedUpDiagonals:
        return False
    if row - col in blockedDownDiagonals:
        return False
    return True
