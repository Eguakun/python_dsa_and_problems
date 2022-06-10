# formula - 2d array named values

# if weight <= j  -->  values[i][j] = max( (values[i-1][j]), (values[i-1][j-w] + v) )

# otherise if weight is greater than the capacity then values[i][j] = values[i-1][j]

# time complexity: 2d array. Number of columns is number of capacity + 1, rows =number of items + 1
# applying formula for each iteration

# Time complexity: O(Nc) where n is the number of items we have and c is the capacity of the bag we have
# space complexity: O(Nc) because of the 2d array, not going to be doing more than Nc operations with any other operations

def knapsackProblem(items, capacity):
    knapsackValues = [[0 for x in range(0, capacity + 1)] for y in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1][1]  # minus 1 because we have first row of no items so it shifts everything by 1
        currentValue = items[i - 1][0]
        for c in range(0, capacity + 1):
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i - 1][c]
            else:
                knapsackValues[i][c] = max(knapsackValues[i - 1][c], knapsackValues[i - 1][c - currentWeight] + currentValue)
    return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]

def getKnapsackItems(knapsackValues, items):
    sequence = []
    i = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1
    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            i -= 1
        else:
            # because just like above because we have an additional row, everything was shifted by 1
            sequence.append(i - 1)
            # we know that in our knapsack we have our item at i -1 , so remove the weight from our current capacity
            c -= items[i - 1][1]
            i -= 1
        if c ==0:
            break
    return list(reversed(sequence))



