# we are going to keep track of the rows and columns in some sort of array and
# we wil also keep track of diagonals only 2 diagonals
# what were going to do is, move through the moves and we will have some sort of boolean
# that keeps track of which player it is, we wil have player 1 be postiive or True
# player 2 will be negative or false

# this is a n*n solution and it also takes n*n space

def tictactoe(moves):
    n = 3
    rows, cols = [0] * n, [0] * n
    diagonal1, diagonal2 = 0,0
    player = 1 # 1 for player 1 and negative 1 for player 2

    for r, c in moves:
        # player 1 we increase it by 1 and player 2 we decrease it by 1
        rows[r] += player
        cols[c] += player

        if r==c:  # meaning its 0,0 1,1 or 2,2 we are going to increase our diagonal 1 by player
            diagonal1 += player

        if r + c == n - 1:  # meaning 1,1 or 2,0 or 0,2 we will do the same thing here
            diagonal2 += player
            # we know there is a winner when the rows, columns , or diagonals have 3 as the value meaning 3 of the same value/same player moves in a row
        if abs(rows[r]) == n or abs(cols[c]) == n or abs(diagonal1) == n or abs(diagonal2) == n:
            if player == 1:
                return "A"
            else:
                return "B"
        player *= -1

        # if we don't find a winner that means that we filled up all the boxes or there are moves to be made:
        # if the moves array is full with all possible moves we return draw
        # otherwise pending

    if len(moves) == (n*n):
        return "Draw"
    else:
        return "Pending"


