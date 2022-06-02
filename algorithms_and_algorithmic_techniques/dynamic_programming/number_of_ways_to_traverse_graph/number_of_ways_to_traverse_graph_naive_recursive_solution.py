# lends itself really well to recursion

# dynamic programming approach
# avoid redundant work
# store intermediate answers of our problems

# algorithm is from the end square, you only can enter it from the top or from the left.
# so if we add up the number of ways to get to the square on top of the end square and to the left of the end square,
# we can get the number of ways to get to the end square. We repeat this logic recursively for every square
# and store intermediate results to avoid redundant calls

# number of ways to get to the bottom right square = (number of ways to get to the square on top + number of ways to get to the square to the left)

# Time Complexity: O(n * m) --> need to look through all of the rows and all of the columns
# Space Complexity: O(n * m) --> need another data strcture to store intermediate results


# Clever math trick solution:

# permutations - unique ordering of elements that are in a set
# can only move right and down
# if width is equal to four, how many times do we need to move right to get to the end
# just if we were to count up the number of right movements,
# right movements = width - 1

# how many down movements ? --> height - 1
# {R, R, R, D, D} --> generate all possible permutations of these movements
# that will tell us the number of ways that we can start at the starting position and reach the end
# if we move right 3 times and move down 3 times, we end up reaching the end position

# theres a really clever formula that gives you the number of permutations, given a set
# (number of right movements + number of down movements)! // (!R * !D)
# number of permutations = ((R + D)! / (R! * D!))

# Time complexity: O(n + m) time
# Space complexity: O(1) space
# ------------------------------


# O(2 ^(n+m)) time | O(n+M) space
# Solution 1: (Naive recursive solution) --> bad time complexity
def numberOfWaysToTraverseGraphRecOne(width, height):
    if width == 1 or height == 1:
        return 1

    return numberOfWaysToTraverseGraphRecOne(width - 1, height) + numberOfWaysToTraverseGraphRecOne(width, height - 1)