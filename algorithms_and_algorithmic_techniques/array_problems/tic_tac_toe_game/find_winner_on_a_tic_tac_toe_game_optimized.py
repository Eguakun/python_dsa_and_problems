
#  v
# A = [0,0,0,0,0,0,0,0]
# B = [0,0,0,0,0,0,0,0]

# A[0] = 0th row
# A[1] = 1st row
# A[2] = 2nd row

# A[3] = 0th column
# A[4] = 1st column
# A[5] = 2nd column

# A[6] = Primary Diagonal
# A[7] = Secondary Diagonal
# -----------------------------------
# B[0] = 0th row
# B[1] = 1st row
# B[2] = 2nd row

# B[3] = 0th column
# B[4] = 1st column
# B[5] = 2nd column

# B[6] = Primary Diagonal
# B[7] = Secondary Diagonal

# Moves = [[0,0], [2,0], [1,1], [2,1], [2,2]]


#
#    a     b     c
#       |     |
# 1  -  |  -  |  -
#  _____|_____|_____
#       |     |
# 2  -  |  -  |  -
#  _____|_____|_____
#       |     |
# 3  -  |  -  |  -
#       |     |

# First move is 0,0 by player A which has the X

#
#    1     2     3
#       |     |
# 1  X  |  -  |  X
#  _____|_____|_____
#       |     |
# 2  -  |  X  |  X
#  _____|_____|_____
#       |     |
# 3  -  |  -  |  X
#       |     |

# When [0,0] is placed on the board for A, we update A's array

# A = [1,1,1,1,1,1,0,0]
# B = [1,0,1,0,1,1,0,0]

# Once we hit 3 1s in a row in either array, we know that the winner is A.
# or if we get a 3 in the diagnoals number

# If X or O is placed in [[0,0], [1,1], [2,2]] -->  increment primary diagonal
# If X or O is placed in [[0,2], [2,0], [1,1]] --> increment secondary diagonal

# doing all 8 checks at the exact same time.

# if we iterate through a and b, we dont return a winner, and they are filled in all the boxes, there is a draw
# if we iterate through a and b, we dont return a winner, and they are NOT filled in all the boxes, return pending

class Solution:
    def tictactoe(self,moves):
        a, b = [0] * 8, [0] * 8
        for idx in range(len(moves)):
            # if were at even index, it is X turn player 1,
            # if were at off index, it is O turn player 2.
            row, col = moves[idx]

            # who is playing right now?
            if idx % 2 == 0:
                player = a
            else:
                player = b

            # account for the row
            player[row] += 1

            player[col + 3] += 1

            if row == col:
                player[6] += 1
            if row == 2 - col:
                player[7] += 1

        for i in range(len(a)):
            if a[i] == 3:
                return "A"
            elif b[i] == 3:
                return "B"
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"




