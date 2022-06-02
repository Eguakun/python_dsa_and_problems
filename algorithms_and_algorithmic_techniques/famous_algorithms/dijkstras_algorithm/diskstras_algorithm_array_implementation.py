# when considering using dijsktras to compute the shortest path
# dijsktras can be used on weighted/unweighted edges and directed/undirected graphs and positive/negative weights
# the implementation is different for each so these are things you need to consider

# we are given a graph and we are given a start vertex and we need to output the shortest path from start vertex to all other vertices in the graph

# in this implementation, we have positive weights, a directed graph, and no self loops


# whatever the length of our adjacency list is represents how many nodes were going to have in our graph

# the key to why dijsktras algorithm works:
# - it keeps track of the already found shortest distances so you dont have to keep viewing the nodes
# that have already had their shortest path calculated
# it allows you to skip paths that you already know are too long. if you have a 14 path option and already calculated a 30 for your other path,
# you know 14 is the choice and you dont have to even traverse it to find out. that may be the only way to solve this


# we need to be able to determine at each iteration which node has the shortest current distance to it

# O(v^2 + e) time complexity | O(v) space complexity - v is number of vertices
def dijkstras_algorithm(start, edges):
    # defined a variable to hold the number of vertices which  is equal to the number of edges
    numberOfVertices = len(edges)
    # list that stores min distances for all vertices
    minDistances = [float("inf") for _ in range(numberOfVertices)]
    # the distance to get to the start vertex is always zero
    minDistances[start] = 0

    visited = set()
    # we terminate when the length of what is visited is equal to the number of vertices
    while len(visited) != numberOfVertices:
        # grabs vertex from our list with the min value that has not yet been visited
        vertex, currentMinDistance = getVertexWithMinDistance(minDistances, visited)
    # if the distance to this vertex equals infinity, we can go ahead and stop the algorithm bc we know that there is no way to get to that vertex
    # we would already have reached it if we could have
        if currentMinDistance == float('inf'):
            break
            # add the vertex to the visited set
        visited.add(vertex)

        for edge in edges[vertex]:
            destination, distanceToDestination = edge

            if destination in visited:
                continue

            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]
            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance

    # look at our min distances list and replace any inf with -1 denoting we couldnt reacvh that vertex
    return list(map(lambda x: -1 if x == float('inf') else x, minDistances))


def getVertexWithMinDistance(distances, visited):
    currentMinDistance = float('inf')
    vertex = None

    for vertexIdx, distance in enumerate(distances):
        if vertexIdx in visited:
            continue
        if distance <= currentMinDistance:
            vertex = vertexIdx
            currentMinDistance = distance
    return vertex, currentMinDistance



