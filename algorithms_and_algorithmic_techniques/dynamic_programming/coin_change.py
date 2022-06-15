# make an array of length n called ways
# iterate through this array and at each index, calculate number of ways that you can get to index amount of dollars
# store this value at each index in the ways array

# formula in a general case:
# whenever we iterate
# if denom is less than or equal to our amount then ways [amount] += ways[amount - denom]


# Time complexity: O(Nd) iterating through denominations and for each denom we iterate through array of n + 1
# Space complexity:O(N)

def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n + 1)]
    ways[0] = 1

    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]

