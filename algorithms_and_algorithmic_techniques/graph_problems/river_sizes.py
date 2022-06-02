# time complexity: O(W * H) or O(n) where n is the total number of nodes
# W = Width of the matrix
# H = Height of the matrix

# space complexity:
# O(W * H)
# because were gonna be building this aux data structure which is
# matrix that holds booleans false/true determining whether or not node is visited.

def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])): # because they dont have same width and height necessarily
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return sizes

def traverseNode(i, j, matrix, visited, sizes):
    # Depth First Search - Iterative
    currentRiverSize = 0

    # stack
    nodesToExplore = [[i, j]]

    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True # mark as visited
        if matrix[i][j] == 0: # if this is land, skip it
            continue
        currentRiverSize += 1
        # unvisited neighbors dont affect space complexity, neither does nodes to explore, never have more nodes in array than total number of nodes in the matrix
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)

def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisited_neighbors = []
    # check that 4 neighbors are potentially valid neighbors.
    if i > 0 and not visited[i - 1][j]:
        unvisited_neighbors.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisited_neighbors.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisited_neighbors.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisited_neighbors.append([i, j + 1])
    return unvisited_neighbors




