# the first thing that we do is traverse the top border,
# then the right border,
# then the bottom border,
# finally the left border
# the perimeter of the array

# then we traverse the perimeter of the array thats contained inside this outer perimeter
# we can solve this problem by treating it as the traversal of a sequence of perimeters of two dimensional arrays
# or eventually possibly, one dimensional arrays once you reach the middle


# we can label  starting row, ending row, starting column, ending column
# iterating through the starting row is as simple as a for loop
# at each column, we add to our final array, the value in the two dimensional array at the starting row and at the given column
# for every column starting at teh starting column going to the ending column inclusive, iterate and grab teh value at the first row

# how do we go down?
    # - for loop --> start at starting row plus one
    # from starting row to ending row, grab all of the values for whatever row were at at the ending column and add them to our array

# how do we go left?
    # - iterate in reverse order between our ending column and our starting column on the final row
    # we will start at ec - 1, so we dont double count

# how do we go up?
    # - iterate through the rows between the ending row and the starting row,
# grab the values from the starting column except the startung row and ending row
    # start from er - 1 and iterate to starting row + 1

# now we need to do this to the inner array -->
    # starting row is going to go down 1,
    # starting column is going to go to the right one,
    # ending column is going to go to the left one
    # ending row is going to go up one

# then we implement the same logic as before
# Time complexity: O(N) where n is the total number of elements in the two dimensional array
# Space complexity: O(N) space since we are storing all values in the array
# and if we werent iterative would be O(1) and recursive would be O(n) due to calls on the call stack



def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        for col in reversed(range(startCol, endCol)):
            result.append(array[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            result.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
    return result







